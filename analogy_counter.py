bias_total = 0
bias_bias = 0
debias_total = 0
debias_bias = 0

with open('labeled.txt') as f1:
    with open('non_labeled.txt') as f2:  
        for line1, line2 in zip(f1, f2):
            label = line1.split()[1]
            vote = line2.split()[1]
			
            if label == "b":
                if vote == "b":
                    bias_bias += 1
				
                bias_total += 1
            else:
                if vote == "b":
                    debias_bias += 1
                
                debias_total += 1
				
bias_percent_before = (bias_bias/bias_total)*100
bias_percent_after = (debias_bias/debias_total)*100

print("The percent of analogies voted to contain a gender sterotype before debiasing: % 2d" %(bias_percent_before)) 
print("The percent of analogies voted to contain a gender sterotype after debiasing: % 2d" %(bias_percent_after)) 


	   