def isIn(char, aStr):
    pos = len(aStr)/2 
    print pos,aStr
    if len(aStr) >= 1:
        if char == aStr[pos]:
            return True   
        elif aStr[pos] > char:
            return isIn(char,aStr[:pos])
        else:
            return isIn(char, aStr[(pos+1):])
    else:
        return False
