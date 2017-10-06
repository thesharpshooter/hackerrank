#!/bin/python

import sys

def maximumToys(prices, k,n):
    prices = sorted(prices)
    i = 0
    count = 0
    while i < n and k > prices[i]:
        k -= prices[i]
        i += 1
        count += 1
    return count
    # Complete this function

if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    prices = map(int, raw_input().strip().split(' '))
    result = maximumToys(prices, k,n)
    print result

