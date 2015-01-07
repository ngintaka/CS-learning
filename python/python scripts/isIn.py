##def isIn(char, aStr):
##    pos = len(aStr)/2
##    guess = aStr[pos]
##    print pos, guess
##    if guess == char:
##        return True
##    elif guess > char:
##        isIn(char, aStr[:(pos)])
##    elif guess < char:
##        isIn(char, aStr[pos+1:])

def isIn(char, aStr):
    guess = ''
    if aStr:
        pos = len(aStr)/2
        guess = aStr[pos]
        print aStr, pos, guess
        if guess == char:
            return True
        else:
            
            if guess > char:
               isIn(char, aStr[:(pos)])
        
            else:
                isIn(char, aStr[pos+1:])
        
    else:
        return False

isIn('l', 'cclrttx')

