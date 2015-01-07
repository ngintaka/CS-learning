# 6.00 Problem Set 3
# 
# Hangman game
# FINAL WORKING VERSION!!!

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
lettersGuessed = []

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    ans = 0
    for i in secretWord:
        if i not in lettersGuessed:
            ans += 1
        else:
            ans += 0
    if ans >0:
        return False
    else:
        return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    s = ''
    for i in secretWord:
        if i not in lettersGuessed:
            s = s + ' _ '
        else:
            s = s + i
    return s

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    s = string.ascii_lowercase
    ans = ''
    for i in s:
        if i not in lettersGuessed:
            ans = ans + i
    return ans
    

def hangman(secretWord):
    guesses = 8
    lettersGuessed = []
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word",len(secretWord),"letters long."
    print "---------- "
    while not isWordGuessed(secretWord,lettersGuessed):
        if guesses < 1:
            print 'Sorry, you ran out of guesses. The word was',secretWord,'.'
            break
        
        print "You have",guesses,"guesses left."
        print "Available letters: ",getAvailableLetters(lettersGuessed)
        guess = raw_input("Please guess a letter: ").lower()
        if guess in lettersGuessed:
            print"Oops! You've already guessed that letter:",getGuessedWord(secretWord,lettersGuessed)
            print "---------- "
        elif guess in secretWord:
            lettersGuessed.append(guess)
            if isWordGuessed(secretWord,lettersGuessed):
                print 'Good guess:',getGuessedWord(secretWord,lettersGuessed)
                print '-----------'
                print 'Congratulations! You won' 
            else:  
                print 'Good guess:',getGuessedWord(secretWord,lettersGuessed)
                print '-----------'
        else:
            lettersGuessed.append(guess)
            print 'Oops! That letter is not in my word:',getGuessedWord(secretWord,lettersGuessed)
            print '-----------'
            guesses -= 1


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
