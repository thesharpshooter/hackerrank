#!/bin/python
def partition(arr):
    p = arr[0]
    left = []
    mid = [p]
    right = []
    for i in range(1,len(arr)):
        if arr[i] < p:
            left.append(arr[i])
        elif arr[i] == p:
            mid.append(arr[i])
        else:
            right.append(arr[i])
    print " ".join(map(str,left+mid+right))
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)

