# -*- coding: utf-8 -*-

from slackbot.bot import respond_to
import sqlite3
import random

@respond_to("もちもち")
def motimoti(message):
    message.reply("モチモチモチモチモﾁﾓﾁﾓﾁﾓ(ﾉ)`ω´(ヾ)(ﾉ)・ω・(ゞ) もちもちモチモチﾓﾁﾓﾁﾓ(ﾉ)`ω´(ヾ)(ﾉ)`ω´(ヾ)ﾓﾁｯモチモチモチモチモﾁﾓﾁﾓﾁﾓ(ﾉ)`ω´(ヾ)(ﾉ)・ω・(ゞ) もちもちモチモチモチモチモﾁﾓﾁﾓﾁﾓ(ﾉ)`ω´(ヾ)(ﾉ)'∨'(ヾ)ﾓﾁﾓﾁ(ﾉ)･∀･(ヾ)ﾓﾁﾓﾁモチモチﾓﾁﾓﾁﾓ(ﾉ)`ω")

@respond_to("eliza")
def eliza(message):
    # データベースを開く
    dbname = "words.db"
    conn = sqlite3.connect(dbname)
    c = conn.cursor()


    lists = [i for i in c.execute('select * from words')]

    text = ""
    generateNumber = random.randint(2, 6)
    for _ in generateNumber:
        text += random.choice(lists)[0]

    message.reply(text)

    # データベースを閉じる
    conn.close()