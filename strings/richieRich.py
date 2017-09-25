#!/bin/python

import sys

def richieRich(s, n, k):
    s = map(int,list(s))
    curr = n/2 if n%2 ==0 else (n/2)-1
    temp = 0
    counters = []
    while temp < k and curr >= 0:
        if s[curr] > s[n-curr-1]:
            s[n-curr-1] = s[curr]
            temp += 1
            counters.append(curr)
        elif s[curr] < s[n-curr-1]:
            s[curr] = s[n-curr-1]
            temp += 1
            counters.append(curr)
        curr -= 1
    if s != s[::-1]:
        return -1
    curr = 0
    k -= temp
    while k > 0 and curr<n/2:
        if s[curr] != 9 and curr in counters and k >= 1:
            s[curr] = s[n-curr-1] = 9
            k -= 1
        elif s[curr] != 9 and k >= 2:
            s[curr] = s[n-curr-1] = 9
            k -= 2
        curr += 1
    if n%2 and k > 0:
        s[n/2] = 9
    return "".join(map(str,s))
    # Complete this function

n,k = map(int,raw_input().split())
s = raw_input().strip()
result = richieRich(s, n, k)
print(result)

