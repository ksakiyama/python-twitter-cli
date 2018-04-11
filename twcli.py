#!/usr/bin/env python
from __future__ import print_function
import os
import sys
import argparse
import configparser
import json
from requests_oauthlib import OAuth1Session

def main():
    path = os.path.join(os.environ['HOME'], '.twclirc')
    if not os.path.exists(path):
        print("You have to save keys and tokens in ~/.twclirc .")
        sys.exit(1)

    config = configparser.ConfigParser()
    config.read(path)
    config.sections()

    twitter = OAuth1Session(
        config["twcli"]["CONSUMER_KEY"].strip(),
        config["twcli"]["CONSUMER_SECRET"].strip(),
        config["twcli"]["ACCESS_TOKEN"].strip(),
        config["twcli"]["ACCESS_TOKEN_SECRET"].strip())

    args = parse()

    if args.mode in ["timeline", "tl"]:
        url_timeline = "https://api.twitter.com/1.1/statuses/home_timeline.json"

        params = {'count': args.count}
        req = twitter.get(url_timeline, params=params)

        if req.status_code == 200:
            timeline = json.loads(req.text)
            for tweet in timeline:
                print(tweet['user']['name'] + '::' + tweet['text'])
                print(tweet['created_at'])
                print(
                    '-----------------------------------------------------------------------------')
        else:
            print("ERROR: %d" % req.status_code)
    else:
        if args.status == "":
            print("You have to set your tweet content")
            sys.exit(1)

        url_tweet = "https://api.twitter.com/1.1/statuses/update.json"
        params = {'status': args.status}
        req = twitter.post(url_tweet, params=params)
        if req.status_code == 200:
            print("Tweet Succees")
        else:
            print("ERROR: %d" % req.status_code)

    print("program end.")


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', help='timeline(tl) or tweet(tw)')
    parser.add_argument('--status', '-s',  default="", help='')
    parser.add_argument('--count', '-c', type=int, default=5,
                        help='# of tweets to show')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
