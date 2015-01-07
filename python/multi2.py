import random

right = 0
wrong = 0
score = right - wrong

username = raw_input("What is your name?  ")
print "\nOK", username, ", which times table do you want to practice today? Type 0 for ALL.  "
tables = int(raw_input())
tests = int(raw_input("What score do you want to go up to? "))

if tables == 0:
    set = []
    for n in range (2, 15):
        for m in range (6, 15):
            set += [[n, m, 0, 0, 0]]
else:
    set = []
    for n in range(2, 15):
        set += [[n, tables, 0, 0, 0]]      
                
while right - wrong < tests:
    choice = set[random.randrange(len(set))]
    #print choice
    answer = choice[0]*choice[1]
    choice[2] += 1
    
    print "\n\nWhat is", choice[0], "times", choice[1], "?"
    response = input()
    
    if response == answer:
        print "\nCORRECT!", choice[0], "times", choice[1], "equals", choice[0]*choice[1]
        choice[3] += 1
        right += 1
            
    else:
        print "\nSORRY!", username, choice[0], "times", choice[1], "equals", choice[0]*choice[1]
        choice[4] += 1
        wrong +=1
                
    print username, "has", right, "right and", wrong, "wrong."

if wrong != 0:
    print "\n", username, "you got these wrong:"
    for s in range(len(set)):
        if set[s][4] != 0:
            print set[s][0], "times", set[s][1], "equals", set[s][0]*set[s][1]
else: print "\nCongratulations", username, "You got a perfect score!"