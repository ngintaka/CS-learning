balance = 4213
annualInterestRate = .2
monthlyPaymentRate = .04
totalPaid = 0

month = 0
for m in range(12):
    monthlyInterestRate = annualInterestRate/12
    minimumMonthlyPayment = balance * monthlyPaymentRate
    monthlyUnpaidBalance = balance - minimumMonthlyPayment

    month = month + 1
    balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    totalPaid = totalPaid + minimumMonthlyPayment

    print "Month:",month
    print "Minimum Monthly Payment",round(minimumMonthlyPayment,2)
    print "Remaining Balance:",round(balance,2)
print "Total Paid:",round(totalPaid,2)
print "Remaining Balance:",round(balance,2)
