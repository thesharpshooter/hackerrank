#!/bin/python

import sys

def stringConstruction(s):
    return len(set(s))
    # Complete this function

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        s = raw_input().strip()
        result = stringConstruction(s)
        print result


