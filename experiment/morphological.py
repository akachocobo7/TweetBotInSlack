# -*- coding: utf-8 -*-

import pandas as pd
import MeCab

if __name__ == "__main__":
    csv_file = pd.read_csv(filepath_or_buffer="tweets.csv", encoding="utf-8", sep=",")
    
    tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

    cnt = 0
    MAXTWEETS = 100
    for text in csv_file["text"]:
        # RTはのぞく
        if "RT" in text:
            continue

        # 形態素解析
        result = tagger.parse(text)

        # 改行文字で分割
        result = result.split('\n')
        for word in result:
            # 名詞か形容詞の言葉だけ抽出
            if "名詞" in word or "形容詞" in word:
                print(word)
                word = word.split()
                # print(word[0])

        cnt += 1
        if cnt >= MAXTWEETS:
            break