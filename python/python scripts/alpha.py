##alpha = 'abcdefghijklmnopqrstuvwxyz'
##n = 1
##i = 0
##snippet = alpha
##print "initial",snippet
##while len(snippet) > 2:
##    snippet = alpha[i:-n]
##    n = n + 1
##    print snippet
##print "All done!"

##alpha = "abcdefghijklmnopqrstuvwxyz"
##s = "abcwxy"
##snip = alpha
##n = 1
##count = 0
##ans = 0
##for i in range(0,len(alpha)+1):
##    for n in range(0,len(alpha)+1):
##        snip = alpha[i:n]
##        if len(snip) > 1:
##            while snip in(s):
##                print snip

alpha = "abcdefghijklmnopqrstuvwxyz"
snip = alpha
n = 1
count = 0
ans = '1'
for i in range(0,len(alpha)+1):
    for n in range(0,len(alpha)+1):
        snip = alpha[i:n]
        if len(snip) > 1:
            #print snip
            if snip in(s):
                #print snip
                if len(snip) > len(ans):
                 ans = snip
print "Longest substring in alphabetical order is:",ans

