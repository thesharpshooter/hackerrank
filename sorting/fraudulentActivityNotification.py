#!/bin/python

import sys
def getMedian(arr,d):
    if d%2:
        cc = -1
        for i in range(201):
            cc += arr[i]
            if cc >= d/2:
                return i
    cc = -1
    a = None
    b = None
    for i in range(201):
        cc += arr[i]
        if cc >= d/2 -1 and not a:
            a = i
        if cc >= d/2 and not b:
            b = i
            break
    return (a+b)/2.0



def activityNotifications(expenditure, d,n):
    count = 0
    if n>d:
        counter = [0]*201
        for i in range(d):
            counter[expenditure[i]] += 1
        for i in range(d,n):
            med = getMedian(counter,d)
            if expenditure[i] >= 2*med:
                count += 1
            counter[expenditure[i]] += 1
            counter[expenditure[i-d]] -= 1
    return count
    # Complete this function

if __name__ == "__main__":
    n, d = raw_input().strip().split(' ')
    n, d = [int(n), int(d)]
    expenditure = map(int, raw_input().strip().split(' '))
    result = activityNotifications(expenditure, d, n)
    print result

