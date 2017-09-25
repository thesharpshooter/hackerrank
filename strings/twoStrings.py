#!/bin/python

import sys
from collections import Counter
def gameOfThrones(s):
    c1 = Counter(s)
    temp = sum([1 for x in c1.values() if x%2 ])
    if temp <= 1:
        return "YES"
    return "NO"
    # Complete this function

s = raw_input().strip()
result = gameOfThrones(s)
print(result)

