# -*- coding: utf-8 -*-
s = "this a test string"
i = 0 #initalize index position
ans = 0 #initalize answer variable
while i < len(s): #stop when have tested all chars in input string (provided)
    if s[i] == 'a': #test if character in index position is the char ‘a’
        ans = ans + 1 #if find an ‘a’ increment ans variable by count of 1
    elif s[i] == 'e':
        ans = ans + 1
    elif s[i] == 'i':
        ans = ans + 1
    elif s[i] == 'o':
        ans = ans + 1
    elif s[i] == 'u':
        ans = ans + 1
    i = i +1 #increment index position by one space and loop to test next character
print 'Number of vowels:',ans