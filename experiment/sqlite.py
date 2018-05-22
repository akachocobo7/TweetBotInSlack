# -*- coding: utf-8 -*-

import sqlite3
from contextlib import closing

if __name__ == "__main__":
    # データベースにつなぐ
    dbname = "words.db"
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    
    # データベース生成
    c.execute('''CREATE TABLE IF NOT EXISTS words (pos text)''')
    
    
    # データを挿入
    insert_sql = "INSERT INTO words (pos) VALUES (?)"
    c.execute(insert_sql, ("aa",))

    # 変更を反映
    conn.commit()

    for i in c.execute('select * from words'):
        print(i)

    # データベースを閉じる
    conn.close()