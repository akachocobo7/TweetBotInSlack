# -*- coding: utf-8 -*-

import pandas as pd
import MeCab
import sqlite3
import re


if __name__ == "__main__":
    # csvファイルを開く
    csv_file = pd.read_csv(filepath_or_buffer="tweets.csv", encoding="utf-8", sep=",")

    tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')


    # データベースにつなぐ
    dbname = "words.db"
    conn = sqlite3.connect(dbname)
    c = conn.cursor()


    # データベースを作ってなければ生成
    c.execute('''CREATE TABLE IF NOT EXISTS words (pos text)''')
    

    cnt = 0
    MAXTWEETS = len(csv_file["text"])
    # print(len(csv_file["text"]))
    for text in csv_file["text"]:
        cnt += 1
        if cnt > MAXTWEETS:
            break

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
                # print(word)
                word = word.split()
                # print(word[0])

                # 数字と英字を取りのぞく
                tmp = re.sub("[0-9a-zA-Z]", "", word[0])

                # すでにデータベースに入っているか検索
                c.execute("SELECT * FROM words WHERE pos=?", (tmp,))
                if c.fetchone() == None:
                    # 入っていない時は挿入
                    insert_sql = "INSERT INTO words (pos) VALUES (?)"
                    insert_data = (tmp,)
                    c.execute(insert_sql, insert_data)
        
    # 変更を反映
    conn.commit()

    for i in c.execute('select * from words'):
        print(i)

    # データベースを閉じる
    conn.close()