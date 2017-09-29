#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
x = map(int,raw_input().strip().split(' '))
x = sorted(x)
i = 0
count = 0
while i < n:
    curr = x[i]
    j = i+1
    while j < n and x[j]-curr <= k:
        j += 1
    i = j-1
    l = i+1
    while l<n and x[l]-x[i] <= k:
        l += 1
    count += 1
    i = l
print count







