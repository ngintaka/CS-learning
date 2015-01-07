balance = 4773
annualInterestRate = .2
totalPaid = 0
month = 0
monthlyPayment = 0
monthlyInterestRate = annualInterestRate/12
m = 0

while m < 12:
    monthlyPayment = monthlyPayment + 10
    monthlyUnpaidBalance = balance - monthlyPayment
    balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    
print monthlyPayment, balance
