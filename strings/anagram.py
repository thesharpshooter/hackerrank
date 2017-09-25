#!/bin/python

import sys
from collections import Counter
def anagram(s):
    n = len(s)
    if n%2:
        return -1
    l = Counter(s[:n/2])
    r = Counter(s[n/2:])
    count = 0
    for x in r:
        curr = r[x] - l[x] if x in l else r[x]
        if curr > 0:
            count += curr
    return count
    # Complete this function

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = anagram(s)
    print(result)


