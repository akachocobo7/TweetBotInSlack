# -*- coding: utf-8 -*-

import sqlite3

if __name__ == "__main__":
    # データベースにつなぐ
    dbname = "example.db"
    conn = sqlite3.connect(dbname)

    c = conn.cursor()

    """
    # データベース生成
    c.execute('''CREATE TABLE character
             (name text, age int)''')
    """
    
    # データを挿入
    # c.execute("INSERT INTO character VALUES ('hoge', 18)")

    # 変更を反映
    conn.commit()

    for i in c.execute('select * from character'):
        print(i)

    # データベースを閉じる
    conn.close()