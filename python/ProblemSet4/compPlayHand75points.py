def compPlayHand(hand, wordList, n):
    wordScore = 0
    finalScore = 0

    while compChooseWord(hand,wordList,n):
    
        print 'Current hand:',
        displayHand(hand)
        
        word = compChooseWord(hand,wordList,n)

        wordScore = getWordScore(word,n)
        finalScore = finalScore + wordScore
        printWord = str(word)
        print ('"%s"')%word,'scored',wordScore,'points. Total:',finalScore,'points', '\n'
        hand = updateHand(hand,word)      

    else:
        print 'Current hand:',
        displayHand(hand)
        print 'Total score:',finalScore,'points'
        
def compChooseWord(hand, wordList, n):
    
    maxScore = 0
    bestWord = None
    for w in wordList:
        if isValidWord(w,hand,wordList):
            wordScore = getWordScore(w,n)
            if wordScore > maxScore:
                maxScore = wordScore
                bestWord = w
    return bestWord
