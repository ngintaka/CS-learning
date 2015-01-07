def sampleQuizzes():
    import random
    
    numTrials = 10000
    trialScores = []
    
    for t in range(numTrials):
        mid1 = random.randrange(50,81)
        mid2 = random.randrange(60,91)
        final = random.randrange(55,96)
    
        trialScores.append(mid1*0.25 + mid2*0.25 + final*0.5)
    #print "Trial scores =", trialScores
    
    count = 0.0
    for s in trialScores:
        if 70 <= s <= 75:
         count += 1
    #print "count", count    
    
    print "Probability =", count / numTrials        