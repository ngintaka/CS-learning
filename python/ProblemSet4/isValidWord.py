def isValidWord(word, hand, wordList):

    copyHand = hand.copy()

    if word not in wordList:
        return False
    else:
        for l in word:
            if l not in copyHand:
                return False
            else:    
                copyHand[l] = copyHand[l]-1
                for k, v in copyHand.items():
                    if v == 0:
                        del copyHand[k]
    return True
            
isValidWord('jpearly', {'a':1, 'p':2, 'l':2, 'e':1, 'z':1},['jpearly', 'apple', 'dog', 'trees', 'apples', 'snapple'])
