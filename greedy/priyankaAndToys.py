# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
arr = sorted(map(int,raw_input().split()))
count = 0
curr = arr[0]
i = 0
while i < n:
    curr = arr[i]
    while i<n and arr[i] <= curr+4:
        i += 1
    count += 1
print count


