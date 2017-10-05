# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n = int(raw_input())
arr = sorted(map(int,raw_input().split()))
max_ = -1
res = []
for i in range(n-2):
    j = i+1
    k = n-1
    while j < k:
        if arr[i]+arr[j] > arr[k] :
            if arr[i]+arr[j]+arr[k] >= max_:
                max_ = arr[i]+arr[j]+arr[k]
                res.append([arr[i],arr[j],arr[k]])
            j += 1
        elif arr[i]+arr[j] <= arr[k]:
            k -= 1
if max_ == -1:
    print max_
else:
    res = filter(lambda x : sum(x) == max_,res)
    res = sorted(res,key = lambda x : x[-1])
    for x in res:
        if x[-1] == res[-1][-1]:
            print " ".join(map(str,x))
            sys.exit()

