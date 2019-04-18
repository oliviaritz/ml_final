import random

#initialize biased and debiased lists (will be provided after running debias algorithm for each)
b_list = [("me", "you", 3.14), ("cat", "dog", 3.14), ("hokie", "hoo", 3.14), ("dorito", "cheeto", 3.14)]
db_list = [("hot", "cold", 3.14), ("yes", "no", 3.14), ("hokie", "hoo", 3.14), ("in", "out", 3.14)]

#add labels
b_list = [list(tup)+["b"] for tup in b_list]
db_list = [list(tup)+["db"] for tup in db_list]

#randomize biased and debiased lists together
mixed_list = b_list + db_list
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


