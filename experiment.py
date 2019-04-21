from __future__ import print_function, division
#matplotlib inline
from matplotlib import pyplot as plt
import json
import random
import numpy as np

import debiaswe as dwe
import debiaswe.we as we
from debiaswe.we import WordEmbedding
from debiaswe.data import load_professions
from debiaswe.debias import debias



E = WordEmbedding('./embeddings/glove.6B.50d_small.txt')

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
a_gender = E.best_analogies_dist_thresh(v_gender)

print("ANALOGIES BEFORE")
for (a,b,c) in a_gender:
    print(a+"-"+b)
	

debias(E, gender_specific_words, defs, equalize_pairs)


# gender analogies after debiasing
a_gender_db = E.best_analogies_dist_thresh(v_gender)

print("ANALOGIES AFTER")
for (a,b,c) in a_gender_db:
    print(a+"-"+b)
