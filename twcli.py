#!/usr/bin/env python
from __future__ import print_function
import os
import sys
import configparser
import json
from requests_oauthlib import OAuth1Session
import fire


class Twcli(object):
    def __init__(self):
        path = os.path.join(os.environ['HOME'], '.twclirc')
        if not os.path.exists(path):
            print("You have to save keys and tokens in ~/.twclirc .")
            sys.exit(1)

        config = configparser.ConfigParser()
        config.read(path)
        config.sections()

        self.__twitter = OAuth1Session(
            config["twcli"]["CONSUMER_KEY"].strip(),
            config["twcli"]["CONSUMER_SECRET"].strip(),
            config["twcli"]["ACCESS_TOKEN"].strip(),
            config["twcli"]["ACCESS_TOKEN_SECRET"].strip())

    def timeline(self, count=5):
        url_timeline = "https://api.twitter.com/1.1/statuses/home_timeline.json"
        params = {'count': count}
        req = self.__twitter.get(url_timeline, params=params)

        if req.status_code == 200:
            timeline = json.loads(req.text)
            for tweet in timeline:
                print(tweet['user']['name'] + '::' + tweet['text'])
                print(tweet['created_at'])
                print('------------------------------------'
                      + '-----------------------------------------')
        else:
            print("ERROR: %d" % req.status_code)

    def tl(self, count=5):
        self.timeline(count)

    def tweet(self, status):
        url_tweet = "https://api.twitter.com/1.1/statuses/update.json"
        params = {'status': status}
        req = self.__twitter.post(url_tweet, params=params)
        if req.status_code == 200:
            print("Tweet Succees")
        else:
            print("ERROR: %d" % req.status_code)

    def tw(self, status):
        self.tweet(status)


def main():
    fire.Fire(Twcli(), name="twcli")


if __name__ == '__main__':
    main()
