#!/bin/python

import sys

def theLoveLetterMystery(s):
    n = len(s)
    count = 0
    a= s[:n/2]
    b = s[-(n/2):][::-1]
    for i in range(len(a)):
        count += abs(ord(a[i])-ord(b[i]))
    return count
    # Complete this function

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = theLoveLetterMystery(s)
    print(result)


