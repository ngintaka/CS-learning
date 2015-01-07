def playHand(hand, wordList, n):

    wordScore = 0
    finalScore = 0

    while calculateHandlen(hand) != 0:
    
        print 'Current hand:',displayHand(hand)
        
        word = raw_input('Enter word, or a "." to indicate that you are finished: ')

        if word == '.':
            print 'Goodbye! Total score:',finalScore,'points'
            break

        else:
            if isValidWord(word,hand,wordList) == False:
                print'Invalid word, please try again.'
                print

            else:
                wordScore = getWordScore(word,n)
                finalScore = finalScore + wordScore
                printWord = str(word)
                print ('"%s"')%word,'scored',wordScore,'points. Total:',finalScore,'points', '\n'
                hand = updateHand(hand,word)      

    else:
        print '\n','Run out of letters. Total score:',finalScore,'points'









def displayHand(hand):
    #print 'Current Hand:',
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
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


def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    lettScore = 0
    bonus = 0
    wordScore = 0

    if len(word) == n: # award bonus for use of all letters
        bonus = 50

    for l in word:
      lettScore = lettScore + SCRABBLE_LETTER_VALUES[l] # increment score for each letter found in word

    return ((lettScore * len(word)) + bonus) #simple arithmetic to generate final word score


def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    newHand = hand.copy() # protect original hand

    for l in word:
        if l in newHand:
            newHand[l] = newHand[l]-1 # decrement values by 1 each time letter found in word

    for k, v in newHand.items(): # find & delete any keys with a zero value (to clean up dict)
        if v == 0:
            del newHand[k]

    hand = newHand
    return hand


def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    letters = 0
    for k, v in hand.items():
        letters = letters + v
    return letters



SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


playHand({'c':1,'e':2,'f':2,'o':1},['coffee','cab','bat','stab'],7)
