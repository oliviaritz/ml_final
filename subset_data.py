import enchant
import re

from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS

d = enchant.Dict("en_US")

with open("./embeddings/glove.6B.50d.txt", "r", encoding='utf8') as f:
    lines = f.readlines()
	
with open("./embeddings/glove.6B.50d_small.txt", "w", encoding='utf8') as f:
    for line in lines:
        word = line.split()[0]
        contains_num = bool(re.search(r'\d', word))
        if d.check(word):
		    if word == "he" or word == "she":
                f.write(line)
            else if not contains_num and not in ENGLISH_STOP_WORDS:
                f.write(line)