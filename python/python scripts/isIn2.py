def isIn(char, aStr):
    pos = len(aStr)/2
    print pos

    if char <= aStr[pos]:
        return True

    elif len(aStr) == 1:
        return False


    elif aStr[pos] > char:
        return isIn(char,aStr[:pos])

    else:
        return isIn(char, aStr[(pos+1):])
isIn('a','')
