#!/usr/bin/env python

"""
Problem 4

Write a Python function that returns True if aString is a palindrome
(reads the same forwards or reversed) and False otherwise. 
Do not use Python's built-in reverse function or aString[::-1] 
to reverse strings.

"""


def isPalindrome(s):
    '''
    aString: a string
    '''
    # Your code here
    import string
    
    def to_chars(s):
        s = s.lower()
        ans = ''.join([ch for ch in s if ch in string.ascii_lowercase])
	return ans

    def is_pal(s):
        if len(s) < 1:
            return True
        else:
	    return s[0] == s[-1] and is_pal(s[1:-1]) 
   
    return is_pal(to_chars(s))




if __name__=="__main__":
    words = ('ala', 'dupa', 'Gommog', 'Bullet', 'BUllellub')
    for word in words:
        print("Word: {} is palidrome? - {}".format(word, isPalindrome(word)))

 
