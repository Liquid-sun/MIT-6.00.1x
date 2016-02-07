#!/usr/bin/env python

balance = 5000

annualInterestRate = 0.2
number_of_months = 12

min_pay = 10

total_paid = 0


if __name__=="__main__":
    while True:
        balance = 4773
        total_paid = 0
        for month in range(1, number_of_months+1):
            balance -= min_pay
            interest = (annualInterestRate / float(number_of_months)) * balance       
            balance += interest
            total_paid += min_pay
            #print("Month: {}".format(month))
        print("Remaining balance at the end of the year: {}".format(round(balance, 2)))
        print("Min payment: {}".format(min_pay))
        if balance <= 0:
            break
        else:
            min_pay += 10           



print("Total paid: {}".format(round(total_paid, 2)))
print("Lowest paiment: {}".format(int(min_pay)))
