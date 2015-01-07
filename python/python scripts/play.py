hi = 100
lo = 0
guess = 50
ans = ''

while ans != 'c':
    if ans == "":
        print "Please think of a number between 0 and 100!"
        print "Is your secret number",guess,"?"
        ans = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if ans == 'c':
        break

    elif ans == 'l':
        lo = guess

    elif ans == 'h':
        hi = guess

    else:
        print "Sorry I did not understand your response."
            
    guess = (hi+lo)/2

    print "Is your secret number",guess,"?"
    ans = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

print "Game over. Your secret number is:",guess
