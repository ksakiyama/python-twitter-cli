# Simple Twitter CLI Client

## Overview
以下の２機能ができる、Pythonで作ったすごくシンプルなTwitter CLIクライアントです。
* 自分のタイムラインを表示する
* Tweetを投稿する

## How to use
* 事前準備1
```
$ chmod +x twcli.py
```

* 事前準備2
```
$ touch ~/.twclirc # KEYとTOKENを記載します
```
以下のように記載。Tweetを投稿する場合は、Write権限を付与しているか確認してください。
```
[twcli]
CONSUMER_KEY = XXXXXXXXXXXXXXXXXXXXX
CONSUMER_SECRET = XXXXXXXXXXXXXXXXXXXXX
ACCESS_TOKEN = XXXXXXXXXXXXXXXXXXXXX
ACCESS_TOKEN_SECRET = XXXXXXXXXXXXXXXXXXXXX
```

* タイムラインを10件表示する表示する
```
./twcli.py tl -c 10
```

* Tweetを投稿する
```
./twcli.py tw -s "Hello from Twitter CLI Client"
```

## Motivation
* Twitter APIを試してみたかった
* Twitter APIを試してみたい人の参考プログラムになれば

## Dependencies
```
$ pip install requests requests_oauthlib
```