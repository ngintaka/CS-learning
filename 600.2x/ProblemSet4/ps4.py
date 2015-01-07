# 6.00.2x Problem Set 4

import numpy
import random
import pylab
#from ps3b import *
from ps3b_precompiled_27 import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    numViruses = 200
    steps = 300
    trialResults = [0] * numTrials
    count = numTrials
    
    for n in range(numTrials):
        viruses = [ResistantVirus(0.1, 0.05, {'guttagonol': False}, 0.005) for v in range(numViruses)]
        patient = TreatedPatient(viruses, 1000)
        results = [0] * steps
     
        for t in range(steps):
            if t > 149:
                patient.addPrescription('guttagonol')
            u = patient.update()
            results[t] += u
#        print results
        trialResults[n] = results [-1]     
    
        count -= 1
        print "Trial #", count
    
    pylab.figure(1)
    pylab.hist(trialResults)
    pylab.title("DelayedTreatment")
    pylab.xlabel("viruses")
    pylab.ylabel("# trials")
    pylab.show()
    


#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    numViruses = 100
    initialSteps = 150
    testSteps = 300
    finalSteps = 150
    totalSteps = initialSteps + testSteps + finalSteps
    trialResults = [0] * numTrials
    count = numTrials
    
    for n in range(numTrials):
        viruses = [ResistantVirus(0.1, 0.05, {'guttagonol': False, 'grimpex':False}, 0.05) for v in range(numViruses)]
        patient = TreatedPatient(viruses, 1000)
        results = [0] * totalSteps
     
        for t in range(totalSteps):
            if t > initialSteps + testSteps:
                patient.addPrescription('guttagonol')
                patient.addPrescription('grimpex')
            elif t > initialSteps:
                patient.addPrescription('guttagonol')    
            u = patient.update()
            results[t] += u
#        print results
        trialResults[n] = results [-1]     
    
        count -= 1
        print "Trial #", count
    
    pylab.figure(num = 1, figsize = (10,10))
    pylab.hist(trialResults)
    pylab.title("Test steps = 150")
    pylab.xlabel("viruses")
    pylab.ylabel("# trials")
    pylab.show()   
   

simulationTwoDrugsDelayedTreatment(100)
