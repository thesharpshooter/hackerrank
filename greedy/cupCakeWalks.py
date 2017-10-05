#!/bin/python

import sys


n = int(raw_input().strip())
cal = map(int, raw_input().strip().split(' '))
cal = sorted(cal)[::-1]
res = 0
for i in range(n):
    res += (2**i)*cal[i]
print res
# your code goes here

