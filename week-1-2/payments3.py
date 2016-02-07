#!/usr/bin/env python

balance = 320000

annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12.0
min_pay = balance / 12
max_pay = (balance * (1 + monthlyInterestRate)**12) / 12.0


ans = (min_pay + max_pay) / 2

while(balance <= 0):
    print('pay: ', ans)

    for month in range(1, 13):
	balance -= ans
        interest = (annualInterestRate / 12.0) * balance       
        balance += interest

    print("Remaining balance at the end of the year: {}".format(round(balance, 2)))
    print("Min payment: {}".format(ans))

    if balance > 0:
        min_pay = ans
    else:
        max_pay = ans

        
print("--------------------------------------------")
#print("Lowest Payment: {}".format(round(ans, 2)))
