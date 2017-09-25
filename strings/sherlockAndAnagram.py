#!/bin/python

import sys
from collections import Counter
def sherlockAndAnagrams(s):
    n = len(s)
    count = 0
    bag = {}
    for l in range(1,n):
        for i in range(n-l+1):
            k = frozenset(Counter(s[i:i+l]).items())
            bag[k] = bag.get(k,0)+1
    for k in bag:
        count += (bag[k]*(bag[k]-1))/2
    return count
    # Complete this function

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = sherlockAndAnagrams(s)
    print(result)


