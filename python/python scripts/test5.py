def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    longStr = ''
    shortLen = min(len(s1),len(s2))
    if len(s1) > len(s2):
        longStr = s1
    else:
        longStr = s2
    if longStr:
        tail = longStr[shortLen:]
    else:
        tail = ''
    ans =''
    for i in range(0,shortLen):
        ans = ans + (s1[i] + s2[i])
    return ans + tail
