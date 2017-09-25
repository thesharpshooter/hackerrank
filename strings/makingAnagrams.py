#!/bin/python

import sys
from collections import Counter
def makingAnagrams(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    for x in set(c1).intersection(set(c2)):
        curr = min(c1[x],c2[x])
        c1[x] -= curr
        c2[x] -= curr
    return sum(c1.values())+sum(c2.values())
    # Complete this function

s1 = raw_input().strip()
s2 = raw_input().strip()
result = makingAnagrams(s1, s2)
print(result)

