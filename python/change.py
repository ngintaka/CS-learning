change = int(raw_input("How much: "))
q = 25
d = 10
n = 5
p = 1
Q = 0
D = 0
N = 0
P = 0
while change > 0:
    if change >= q:
        change = change -q
        Q = Q + 1
    elif change >= d:
        change = change - d
        D = D + 1
    elif change >= n:
        change = change - n
        N = N + 1
    elif change >= p:
        change = change - p
        P = P + 1
coins = Q + D + N + P
print "Total coins: ",coins
print "Quarters: ",Q
print "Dimes: ",D
print "Nickels: ",N
print "Pennies: ",P