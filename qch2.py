x = int(raw_input('Enter an integer: '))
ans = 0
while ans**3 < abs(x):
    ans += 1

if ans**3 != abs(x):
    print "not perfect cube"
else:
    if x < 0: ans = -ans
    print('Cube root of {} is {}'.format(x, ans))

