balance = 999999
annualInterestRate = 0.18
initialBalance = balance
int = annualInterestRate/12
hi = (balance*(1+int)**12)/12.0
lo = balance/12
epsilon = 0.01
minPayment = (hi + lo)/2.0
#minPayment = 29157.09
finalBalance = balance
while abs(finalBalance) >= epsilon:
    balance = initialBalance
    for m in range(12):
        balance = (balance - minPayment) + (balance - minPayment) * int
        #print balance
    finalBalance = round(balance,3)
    if abs(finalBalance) <= epsilon:
        #print 'finished'
    elif finalBalance > 0:
        lo = minPayment
    else:
        hi = minPayment
    minPayment = (hi + lo) / 2                   
print 'Lowest payment:',round(minPayment,2)