balance = 4773
annualInterestRate = .2
int = annualInterestRate/12
bal = 1
x = 10
while bal > 0:
    bal = balance
    x = x + 10
    for m in range(12):
        bal = (bal-x) + ((bal-x) * int)
        #print x, bal
print x, bal
