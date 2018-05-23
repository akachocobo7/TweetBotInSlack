# -*- coding: utf-8 -*-

import sqlite3
import random


if __name__ == "__main__":
    # データベースを開く
    dbname = "words.db"
    conn = sqlite3.connect(dbname)
    c = conn.cursor()


    lists = [i for i in c.execute('select * from words')]

    text = ""
    generateNumber = random.randint(2, 6)
    for _ in generateNumber:
        text += random.choice(lists)[0]
    print(text)

    # データベースを閉じる
    conn.close()