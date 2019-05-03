# TweetBotInSlack

ツイートの文章から新しい語録を生み出すbotです。

## 大まかな使い方

- python3をインストール

- mecab-ipadic-NEologdのインストール
```
$ git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
$ cd mecab-ipadic-neologd
$ ./bin/install-mecab-ipadic-neologd -n
```

- mecab-python3のインストール
```
$ pip3 install mecab-python3
```

- TweetBot_in_Slackのダウンロード
```
$ https://github.com/chocobo777/TweetBot_in_Slack.git
$ cd TweetBot_in_Slack
```

- ```.env``` ファイルを作成
```
$ vi .env

SLACK_API=##################################################
```

- twitterから過去のツイートを取得し、tweets.csvをvariousフォルダに置く

- 辞書を生成
```
$ cd verious
$ python3 db.py
$ python3 conversion.py
```


- botの起動
```
$ python3 run.py
```
