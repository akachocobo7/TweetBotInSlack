# -*- coding: utf-8 -*-

import pandas as pd
import MeCab

if __name__ == "__main__":
    csv_f = pd.read_csv(filepath_or_buffer="tweets.csv", encoding="utf-8", sep=",")
    
    tagger = MeCab.Tagger('-Ochasen')

    n = 0
    for text in csv_f["text"]:
        # RTはのぞく
        if "RT" in text:
            continue

        result = tagger.parse(text)
        # print(text)
        print(result)

        if n > 5:
            break
        n += 1