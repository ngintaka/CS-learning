##def laceStrings(s1,s2):
##    longStr = ''
##    shortLen = min(len(s1),len(s2))
##    print 'short len =',shortLen
##    if len(s1) > len(s2):
##        longStr = s1
##    else:
##        longStr = s2
##    print 'longStr =',longStr
##    if longStr:
##        tail = longStr[shortLen:]
##    else:
##        tail = ''
##    print 'tail = ',tail
##    ans =''
##    for i in range(0,shortLen):
##        ans = ans + (s1[i] + s2[i])
##        print 'ans = ',ans
##    print 'ans = ',ans + tail
##    
##
##laceStrings('mmm', '')

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
    return 'ans = ',ans + tail
    


