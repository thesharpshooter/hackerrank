#!/bin/python

import sys

def minimumAbsoluteDifference(n, arr):
    arr = sorted(arr)
    return min([abs(arr[i]-arr[i-1]) for i in range(1,n)])
    # Complete this function

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    result = minimumAbsoluteDifference(n, arr)
    print result

