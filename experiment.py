from __future__ import print_function, division
#matplotlib inline
from matplotlib import pyplot as plt
import json
import random
import numpy as np
from we import WordEmbedding
from debias import debias


E = WordEmbedding('./embeddings/glove.6B.300d_small.txt')

# Lets load some gender related word lists to help us with debiasing
with open('./data/definitional_pairs.json', "r") as f:
    defs = json.load(f)

with open('./data/equalize_pairs.json', "r") as f:
    equalize_pairs = json.load(f)

with open('./data/gender_specific_seed.json', "r") as f:
    gender_specific_words = json.load(f)

# gender direction
v_gender = E.diff('she', 'he')


# gender analogies before debiasing
a_gender = E.best_analogies_dist_thresh(v_gender, 1, 150, 50000)

'''
print("ANALOGIES BEFORE")
for (a,b,c) in a_gender:
    print(a+"-"+b)
'''


debias(E, gender_specific_words, defs, equalize_pairs)


# gender analogies after debiasing
a_gender_db = E.best_analogies_dist_thresh(v_gender, 1, 150, 50000)

'''
print("ANALOGIES AFTER")
for (a,b,c) in a_gender_db:
    print(a+"-"+b)
'''

# mix before and after biasing analogies and write them out to file for voting

#add labels
a_gender = [list(tup)+["b"] for tup in a_gender]
a_gender_db = [list(tup)+["db"] for tup in a_gender_db]

#randomize biased and debiased lists together
mixed_list = a_gender + a_gender_db
random.shuffle(mixed_list)

wout_labels = open('non_labeled.txt','a')
wout_labels.truncate(0)

w_labels = open('labeled.txt','a')
w_labels.truncate(0)

for (a,b,c,d) in mixed_list:
    out1 = a + "-" + b +"\n"
    wout_labels.write(out1)

    out2 = a + "-" + b + " " + d + "\n"
    w_labels.write(out2)

wout_labels.close()
w_labels.close()
