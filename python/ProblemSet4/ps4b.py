from ps4a import *
import time

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

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    
    wordScore = 0
    finalScore = 0
    
    while calculateHandlen(hand) != 0:

            print 'Current hand:',
            displayHand(hand)
        
            if compChooseWord(hand, wordList, n):
                word = compChooseWord(hand,wordList,n)
                wordScore = getWordScore(word,n)
                finalScore = finalScore + wordScore
                printWord = str(word)
                print ('"%s"')%word,'scored',wordScore,'points. Total:',finalScore,'points', '\n'
                hand = updateHand(hand,word)

            else:
                print 'Total score:',finalScore,'points'
                return
    else:
        print 'Total score:',finalScore,'points'
        return
            
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    games = 0
    while True:
        choice1 = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if choice1 == 'e':
            return
        elif choice1 != 'n' or choice1 != 'r':
            print 'Invalid command.'
            playGame
        choice2 = raw_input('Enter u to have yourself play, c to have the computer play: ')
        if choice2 != 'u' or choice2 != 'c':
            print 'Invalid command.'
                
        n = HAND_SIZE

        if choice1 == 'n':
            games = 1
            hand = dealHand(n)
            if choice2 == 'u':
                playHand(hand, wordList, n)
                playGame
            else:
                compPlayHand(hand,wordList,n)
                playGame

        elif choice == 'r':
            if games == 0:
                print 'You have not played a hand yet. Please play a new hand first!'
            else:
                if choice2 == 'u':
                    playHand(hand,wordList,n)
                    playGame
                else:
                    compPlayHand(hand,wordList,n)
                    playGame

    


        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


