#!/usr/bin/env python

s = 'azcboobobegghabokbobl'
#s = ''


start = 0
total = 0
pos = 0

while True:
    pos = s.find('bob', start)
    if pos == -1:
        break
    elif pos != -1:
    	total += 1
    start = pos + 1

print("Number of times bob occurs is: {}".format(total))
