import numpy as np

arr = np.random.choice(["H","T"],size=1000)
countH =0
countT =0
for a in arr:
    if(a=="H"):
        countH += 1
    else:
        countT += 1

P_h = countH/len(arr)
P_t = 1 - P_h 
print("Probability of heads: \n",P_h)
print("Probability of tails: \n",P_t)