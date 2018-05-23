# -*- coding: utf-8 -*-

from slackbot.bot import respond_to
import random

@respond_to("もちもち")
def motimoti(message):
    message.reply("モチモチモチモチモﾁﾓﾁﾓﾁﾓ(ﾉ)`ω´(ヾ)(ﾉ)・ω・(ゞ) もちもちモチモチﾓﾁﾓﾁﾓ(ﾉ)`ω´(ヾ)(ﾉ)`ω´(ヾ)ﾓﾁｯモチモチモチモチモﾁﾓﾁﾓﾁﾓ(ﾉ)`ω´(ヾ)(ﾉ)・ω・(ゞ) もちもちモチモチモチモチモﾁﾓﾁﾓﾁﾓ(ﾉ)`ω´(ヾ)(ﾉ)'∨'(ヾ)ﾓﾁﾓﾁ(ﾉ)･∀･(ヾ)ﾓﾁﾓﾁモチモチﾓﾁﾓﾁﾓ(ﾉ)`ω")

@respond_to("eliza")
def eliza(message):
    # ファイルを開く
    file = open("words.txt", "r")

    words = file.read()
    wordlist = words.split("\n")

    generateNumber = random.randint(2, 6)
    text = ""
    for _ in range(generateNumber):
        text += random.choice(wordlist)

    message.reply(text)

    file.close()