#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    res = -1
    n = int(raw_input().strip())
    a = (n/3)*3
    for i in range((n/3)+1):
        if (n-a)%5 == 0:
            res = "5"*a + "3"*(n-a)
            break
        else:
            a -= 3
    print res

