# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
t = int(raw_input())
for _ in range(t):
    res = "YES"
    n = int(raw_input())
    arr = []
    for i in range(n):
        temp = sorted(raw_input())
        arr.append(temp)
    for j in range(n):
        temp = [arr[i][j] for i in range(n)]
        if temp != sorted(temp):
            res = "NO"
            break
    print res
