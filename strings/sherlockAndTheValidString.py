#!/bin/python

import sys
from collections import Counter
def isValid(s):
    c = Counter(Counter(s).values())
    if len(c) <= 1 :
        return "YES"
    if len(c) == 2:
        curr = list(c)
        if abs(curr[0]-curr[1]) == 1 :
            if c[max(curr[0],curr[1])] == 1:
                return "YES"
        if min(curr[0],curr[1]) == 1 and c[min(curr[0],curr[1])] == 1:
            return "YES"
    return "NO"
    # Complete this function

s = raw_input().strip()
result = isValid(s)
print(result)

