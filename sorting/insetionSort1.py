#!/bin/python
def insertionSort(arr):
    temp = arr[-1]
    i = len(arr)-2
    while i>= 0 and temp<arr[i]:
        arr[i+1] = arr[i]
        print " ".join(map(str,arr))
        i -= 1
    arr[i+1] = temp
    print " ".join(map(str,arr))
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)

