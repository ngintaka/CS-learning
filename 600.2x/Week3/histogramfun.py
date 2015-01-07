import pylab
import numpy as np

# You may have to change this path
WORDLIST_FILENAME = "C:\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    vowels = ["a", "e", "i", "o", "u"]

    bins = {}
    for b in range(numBins):
        bins[b] = 0
        
    for w in wordList:
        vowelCount = 0
        binPos = 0
        for i in range(len(w)):
            if w[i] in vowels:
                vowelCount += 1
            binPos = (vowelCount*1000 / len(w)) / (1000/numBins) #check this calc
        for k in bins:
            if binPos == k:
                bins[k] += 1
    # print bins
    pylab.hist(bins.keys(), weights = bins.values(), bins = numBins)
    pylab.title("Proportion of Vowels in Words in Wordlist")
    pylab.xlabel("Distribution")
    pylab.ylabel("Number of words")
    pylab.show()

    
if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList, numBins =10)
