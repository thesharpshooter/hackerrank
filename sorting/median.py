# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
arr = sorted(map(int,raw_input().split()))
if n%2 == 0:
    print (arr[n/2]+arr[n/2 -1 ])
else:
    print arr[n/2]
