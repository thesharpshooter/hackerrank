# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n,m,k = map(int,raw_input().split())
res = {}
for i in range(k):
    r,c1,c2 = map(int,raw_input().split())
    if r in res:
        temp = (res[r][-1])
        if c1 <= temp[-1]:
            (res[r][-1])[-1] = max(c2,temp[-1])
        else:
            res[r].append([c1,c2])
    else:
        res[r] = [[c1,c2]]
count = n*m
for i in res:
    curr = res[i]
    for j in curr:
        count -= (j[1]-j[0]+1)
print count
