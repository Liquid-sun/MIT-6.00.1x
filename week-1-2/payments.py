#!/usr/bin/env python

balance = 5000

annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate / 12
monthlyPaymentRate = 0.02
number_of_months = 12


total_paid = 0

if __name__=="__main__":
    for month in range(1, number_of_months+1):

        minpay = balance * monthlyPaymentRate
        unpaid_balance = balance - minpay
        interest = (annualInterestRate / float(number_of_months)) * unpaid_balance       
        balance = unpaid_balance + interest
        total_paid += minpay
        print("Month: {}".format(month))
        print("Minimum monthly payment: {}".format(round(minpay, 2)))
        print("Remaining balance: {}".format(round(balance, 2)))
	
print("Total paid: {}".format(round(total_paid, 2)))
print("Remaining balance: {}".format(round(balance, 2)))
