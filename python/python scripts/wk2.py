# this identifies chars in alpha that appear in string s
##alpha = "abcdefghijklmnopqrstuvwxyz"
##s = 'bcegkigf'
##for c in(s):
##    for i in(alpha):
##        if i == c:
##            print i

# can use > operator to identify earlier & later letters in alphabet

##VERSION 2
##alpha = "abcdefghijklmnopqrstuvwxyz"
##s = 'bcegkigf'
##ans = ""
##for c in(s):
##    for i in(alpha):
##        if i == c:
##            ans += str(i) #append to string
##            print i, alpha.index(i) # prints found char and index number in alpha
##print ans

##VERSION 3: finds characters in alpha order, but then stops at latest character. need to step through all substrings.
##alpha = "abcdefghijklmnopqrstuvwxyz"
##s = 'acbobobegghakls'
##ans = ""
##for c in(s):
##    for i in(alpha):
##        if i == c:
##            if len(ans) == 0:
##                ans += str(i)
##            elif i > (ans)[-1]:
##                ans += str(i) #append to string
##                #print i, alpha.index(i) # prints found char and index number in alpha
##print "Longest substring in alphabetical order is:",ans
##

##alpha = "abcdefghijklmnopqrstuvwxyz"
##s = 'ajobobegghakls'
##ans = ""
##init = 0
##for i in(s):
##        if alpha[init] == i:
##            init = init + 1
##        print init, i


##s = 'azcf'
##ans = ""
##i = 1
##t = 0
##for c in (s):
##    if s[1] > s[i-1]:
##        ans = str((s[0] + s[1]))
##        print c, i, ans
##        


s = 'azcf'
n = 1
ans = ""
while s[n] > s[n-1]:
    ans += str((s[n]+s[n-1]))
    
    
    

