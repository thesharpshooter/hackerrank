#!/bin/python

import sys
import heapq
def getMinimumCost(n, k, c):
    c = map(lambda x : -x,c)
    heapq.heapify(c)
    num = {}
    curr = 1
    cost = 0
    for i in range(n):
        hist = num.get(curr,0)
        l = heapq.heappop(c)
        cost += -l*(hist+1)
        num[curr] = hist+1
        curr = (curr+1)%k
    return cost
    # Complete this function

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
c = map(int, raw_input().strip().split(' '))
minimumCost = getMinimumCost(n, k, c)
print(minimumCost)

