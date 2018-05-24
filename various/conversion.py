# -*- coding: utf-8 -*-

import sqlite3

if __name__ == "__main__":
    # データベースにつなぐ
    dbname = "words.db"
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    file = open('words.txt', 'w')


    for word in c.execute('select * from words'):
        file.write(word[0] + "\n")


    file.close()