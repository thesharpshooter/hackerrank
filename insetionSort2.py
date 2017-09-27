#!/bin/python

def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        temp = arr[i]
        j = i-1
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
        print " ".join(map(str,arr))
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)

