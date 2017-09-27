#!/bin/python
def quick_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    p = arr[0]
    left = []
    right = []
    mid = [p]
    for i in range(1,n):
        if arr[i] < p:
            left.append(arr[i])
        elif arr[i] > p:
            right.append(arr[i])
        else:
            mid.append(arr[i])
    arr = quick_sort(left)+mid+quick_sort(right)
    print " ".join(map(str,arr))
    return arr

m = input()
ar = [int(i) for i in raw_input().strip().split()]
temp = quick_sort(ar)

