# Enter your code here. Read input from STDIN. Print output to STDOUT
n,k = map(int,raw_input().split())
arr = map(int,raw_input().split())
res = {}
for i in range(n):
    res[arr[i]] = i
i = 0
while i<n-1 and k > 0:
    if arr[i] != n-i:
        index = res[n-i]
        res[arr[i]] = index
        res[arr[index]] = i
        arr[i],arr[index] = arr[index],arr[i]
        k -= 1
    i += 1
print " ".join(map(str,arr))
