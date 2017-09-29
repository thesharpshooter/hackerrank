# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
arr = map(int,raw_input().split())
arr = sorted(arr)
res = [arr[0],arr[1]]
min_ = arr[1]-arr[0]
for i in range(2,n):
    if arr[i]-arr[i-1] < min_:
        min_ = arr[i]-arr[i-1]
        res = [arr[i-1],arr[i]]
    elif arr[i]-arr[i-1] == min_:
        res.append(arr[i-1])
        res.append(arr[i])
print " ".join(map(str,res))




