
balance = 999999
annualInterestRate = 0.18

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

ans = (upper_bound + lower_bound) / 2.0
bal = balance

while(abs(bal) > 0.01):
    bal = calc_balance(balance, ans)
    if bal > 0:
        lower_bound = ans
    else:
        upper_bound = ans

    ans = (upper_bound + lower_bound) / 2.0


print('Lowest Payment: {:.2f}'.format(ans))
