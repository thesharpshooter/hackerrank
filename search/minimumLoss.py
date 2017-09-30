# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
arr = map(int,raw_input().split())
loss = float("inf")
res = {}
for i in range(n):
    res[arr[i]] = i
temp = sorted(res)
for i in range(1,n):
    if temp[i]-temp[i-1] < loss and res[temp[i-1]] > res[temp[i]]:
        loss = temp[i]-temp[i-1]
print loss


