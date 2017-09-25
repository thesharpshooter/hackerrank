#!/bin/python

import sys

def palindromeIndex(s):
    if s == s[::-1]:
        return -1
    n = len(s)
    for i in range(n/2):
        if s[i] != s[n-i-1]:
            if s[i+1:n-i] == s[i+1:n-i][::-1]:
                return i
            elif s[i:n-i-1] == s[i:n-i-1][::-1]:
                return n-i-1
    return -1
    # Complete this function

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = palindromeIndex(s)
    print(result)


