#!/bin/python

import sys

def solve(a):
    n = len(a)
    if n == 1:
        return "YES"
    sum_ = [0]*n
    sum_[0] = a[0]
    for i in range(1,n):
        sum_[i] = sum_[i-1] + a[i]
    for i in range(1,n-1):
        if sum_[i-1] == sum_[-1]-sum_[i]:
            return "YES"
    return "NO"

    # Complete this function

T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    result = solve(a)
    print(result)


