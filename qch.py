x = int(raw_input('Enter an integer: '))
ans = 0
while ans**3 < x:
    ans += 1

if ans**3 != x: print "not perfect cube"
else: print('Cube root of {} is {}'.format(x, ans))

