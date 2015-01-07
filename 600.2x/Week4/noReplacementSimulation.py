import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''

    count = 0.0
    
    for i in range(numTrials):
        bucket = ['red', 'red', 'red', 'green', 'green', 'green']
        selects = []
        
        for j in range(3):
            x = random.choice(bucket)
            selects.append(x)
            bucket.remove(x)
       
        if selects[0] == selects[1] and selects[0] == selects[2]:
                count += 1
    return count / numTrials    

noReplacementSimulation(5000)