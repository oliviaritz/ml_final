import enchant
import re

from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS

d = enchant.Dict("en_US")

with open("./embeddings/glove.6B.50d.txt", "r", encoding='utf8') as f:
    lines = f.readlines()

count = 0
with open("./embeddings/glove.6B.50d_small.txt", "w", encoding='utf8') as f:
    for line in lines:
        if count == 26000:
            break;

        word = line.split()[0]
        contains_num = bool(re.search(r'\d', word))
        if d.check(word):
            if word == "he" or word == "she":
                f.write(line)
                count += 1
            elif (not contains_num) and (word not in ENGLISH_STOP_WORDS):
                f.write(line)
                count += 1