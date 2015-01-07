import random

print "Type Q to end\n"
right = 0
wrong = 0

while True:
    i = random.randrange(3, 15)
    j = random.randrange(6, 15)
    multi = i*j

    print "What is", i, "times", j, "?"

    answer = input()

    if answer == "Q":
            break
    elif answer == multi:
        print "\nYES!"
        right += 1
    else:
        print "\n
        SORRY"
        wrong += 1

    print i, "times", j, "=", i*j, "\n"
    print "YOUR SCORE Right:", right, " Wrong:", wrong, "\n"