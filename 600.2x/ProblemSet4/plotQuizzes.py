def plotQuizzes():
    import random
    import pylab
    import numpy    
    
    def generateScores(numTrials):
        
        finalScores = []
    
        for t in range(numTrials):
            mid1 = random.randrange(50,81)
            mid2 = random.randrange(60,91)
            final = random.randrange(55,96)
    
            finalScores.append(mid1*0.25 + mid2*0.25 + final*0.5)
     
         
        return finalScores
        
    finalScores = generateScores(10000)
    pylab.figure(1)
    pylab.hist(finalScores, bins =7)
    pylab.title('Distribution of Scores')
    pylab.xlabel('Final Score')
    pylab.ylabel('Number of Trials')
    pylab.show()        