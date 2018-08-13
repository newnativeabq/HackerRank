# -*- coding: utf-8 -*-

import random
import numpy as np

#generate a working input for the analysis
#scores = np.random.randint(100, size=10)
#print(scores)

#scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
#scores = [0, 9, 3, 10, 2, 20]

#Use function notation to describe code as required by assignment
def breakingRecords(scores):
    scorefn = []
    best = 0
    worst = scores[0]
    i=0
    for x in scores: 
        if x < worst:
            scorefn.append(0)
            worst = x
        elif x > best:
            scorefn.append(1+2*(not bool(i)))
            best = x
        else:
            scorefn.append(2)
#        print(i,scorefn.count(1), scorefn.count(0))    
        i=i+1 
#    print(scorefn)
    return scorefn.count(1), scorefn.count(0)

    

print(breakingRecords(scores))