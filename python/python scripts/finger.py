def lenRecur(aStr):
    if aStr == '':
        return 0
    else:
        ans = lenRecur(aStr[:-1])
        ans += 1
    return ans
        
