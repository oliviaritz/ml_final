#import enchant
import re
import json

# cite : https://github.com/dwyl/english-words
with open('./data/words_dictionary.json') as json_file:
    dictionary = json.load(json_file)

with open("./embeddings/glove.6B.300d.txt", "r", encoding='utf8') as f:
    lines = f.readlines()

count = 0
with open("./embeddings/glove.6B.300d_small.txt", "w", encoding='utf8') as f:
    for line in lines:
        if count == 26423:
            break;

        word = line.split()[0]
        contains_num = bool(re.search(r'\d', word))

        if word in dictionary:
            if (not contains_num):
                f.write(line)
                count += 1
