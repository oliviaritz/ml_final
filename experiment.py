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



E = WordEmbedding('./embeddings/glove.6B.50d_small.txt')

# gender direction
v_gender = E.diff('she', 'he')


# analogies gender
a_gender = E.best_analogies_dist_thresh(v_gender)


for (a,b,c) in a_gender:
    print(a+"-"+b)
