#!/bin/python

import sys
def moves(i,j,n):
    res = [[-1 for _ in range(n)] for _ in range(n)]
    res[0][0] = 0
    x = [i,i,j,j,-i,-i,-j,-j]
    y = [j,-j,i,-i,j,-j,i,-i]
    q = [(0,0)]
    while len(q) != 0:
        curr = q.pop(0)
        a,b = curr[0],curr[1]
        for temp in range(8):
            if (0<= a+x[temp] < n) and (0 <= b+y[temp] < n) and (res[a+x[temp]][b+y[temp]] == -1):
                res[a+x[temp]][b+y[temp]] = res[a][b] + 1
                q.append((a+x[temp],b+y[temp]))
    return res[-1][-1]

n = int(raw_input().strip())
res = []
for i in range(1,n):
    temp = []
    for j in range(1,n):
        curr = moves(i,j,n)
        temp.append(curr)
    print " ".join(map(str,temp))
# your code goes here

