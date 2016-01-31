

balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = (annualInterestRate) / 12.0
epsilon = 0.01


def calc_balance(b, payment):
    for month in range(1,13):
        b -= payment
        interest = (annualInterestRate / 12.0) * b
        b += interest
    return round(b, 2)


lower_bound = balance / 12
upper_bound = (balance * ( 1 + monthlyInterestRate)**12)/12.0
r = lambda x: round(x ,2)
ans = (upper_bound + lower_bound) / 2.0
bal = balance

while(bal > 0.01):
    print('low: {}, high: {}, ans:{}'.format(r(lower_bound),
                                             r(upper_bound),
                                             r(ans)))
    bal = calc_balance(balance, ans)
    print("bal", bal)
    if bal > 0:
        lower_bound = ans
    else:
        upper_bound = ans

    ans = round(((upper_bound + lower_bound) / 2.0), 2)
    print("ans: {}".format(ans))


print('--------------------------')
print('Lowest Payment: ', ans)

