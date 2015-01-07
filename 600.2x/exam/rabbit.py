import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 50
CURRENTFOXPOP = 300

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
  
    newBirths = 0
    rabbitPopDensity = float(CURRENTRABBITPOP) / float(MAXRABBITPOP) 
    birthProb = (1.0 - rabbitPopDensity)
       
    for r in range(CURRENTRABBITPOP):
        if birthProb > random.random():
            newBirths += 1
        
    if CURRENTRABBITPOP + newBirths > MAXRABBITPOP:
        CURRENTRABBITPOP = MAXRABBITPOP
        
    else:    
        CURRENTRABBITPOP += newBirths

            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    eatProb = float(CURRENTRABBITPOP) / float(MAXRABBITPOP)
    foxBirthProb = 1.0 / 3.0
    #foxBirthProb = float(1 / 3)
    foxDeathProb = 0.1
    
    for f in range(CURRENTFOXPOP):
            if eatProb >= random.random() and CURRENTRABBITPOP > 10:
                #print 'eat', True
                CURRENTRABBITPOP -= 1
                if foxBirthProb >= random.random():
                    #print 'Birth', True
                    CURRENTFOXPOP += 1
            else:
                if foxDeathProb >= random.random() and CURRENTFOXPOP > 10:
                    #print 'Death', True
                    CURRENTFOXPOP -= 1        
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations = []
    fox_populations = []
    
    for n in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    return (rabbit_populations, fox_populations)

        
def plotData(numSteps):
    (rabbits, foxes) = runSimulation(numSteps)
    steps = [step for step in range(numSteps)]
    print 'steps', steps
#    pylab.plot(rabbits)
#    pylab.plot(foxes)
    foxes = pylab.array(foxes)
    print 'rabbits:', foxes
    steps = pylab.array(steps)
    a,b,c = pylab.polyfit(foxes, steps, 2)
    print a, b, c
    pylab.plot(pylab.polyval(a*steps**2 + b*steps + c,steps))
    