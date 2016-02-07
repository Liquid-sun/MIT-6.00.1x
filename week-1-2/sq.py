#!/usr/bin/env python

x = 25
epsilon = 0.01

step = epsilon**2

num_guesses = 0

ans = 0.0

while (abs(ans**2 - x)) >= epsilon and ans <= x:
    ans += step
    num_guesses += 1

print('num_guesses = {}'.format(num_guesses))

if abs(ans**2-x) >= epsilon:
    print('failed on square root of {}'.format(x))
else:
    print("{} is close to the square root of {}".format(ans, x))


