# -*- coding: utf-8 -*-

import sqlite3
import random


if __name__ == "__main__":
    # ファイルを開く
    file = open('words.txt', 'r')

    words = file.read()
    wordlist = words.split("\n")

    generateNumber = random.randint(2, 6)
    text = ""
    for _ in range(generateNumber):
        text += random.choice(wordlist)

    print(text)

    file.close()