import random

def toss(numTrials):
    count = 0
    for t in range(numTrials):
        results = []
        for f in range(2):
            trial = random.choice([0,1])
            results.append(trial)
                   
        if sum(results) > 0:
            count += 1  
    
    return float(count) / numTrials

print abs(toss(1000000) - 0.750000)