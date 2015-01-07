x = int(raw_input("Give me a number, any number, and I'll attempt to find the square root: "))
epsilon = 0.001
step = epsilon**2
numGuesses = 0
ans = 0.0
while abs(ans**2-x) > epsilon and ans <= x:
    ans += step
    numGuesses += 1
print "total number of guesses was",numGuesses
if abs(ans**2-x) > epsilon:
    print "Failure!"
else:
    print "The square root of",x,"is approximately",ans
        
