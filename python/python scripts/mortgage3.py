balance = 320000
annualInterestRate = 0.2

int = annualInterestRate/12
lo = balance/12
hi = (balance * (1 + int)**12)/12
epsilon = .005
guess = (hi + lo) / 2

while abs(balance) >= round(0):
    for m in range(12):
        balance = ((balance - guess) + (balance - guess)*int)
    if balance > 0:
        lo = guess
    else:
        hi = guess
guess = (hi + lo) / 2
   
