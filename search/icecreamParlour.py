# Enter your code here. Read input from STDIN. Print output to STDOUT
def get(arr,m,n):
    arr = sorted([[arr[i],i] for i in range(n)],key = lambda x :x[0])
    i = 0
    res = [None,None]
    diff = float("inf")
    while i < n-1 and arr[i][0] < m:
        temp = m-arr[i][0]
        j = i+1
        while j < n and temp-arr[j][0]>=0:
            if temp-arr[j][0] < diff:
                diff = temp-arr[j][0]
                res[0] = arr[j][1]
                res[1] = arr[i][1]
                if diff == 0:
                    break
            j += 1
        i += 1
    return res


t = int(raw_input())
for i in range(t):
    m = int(raw_input())
    n = int(raw_input())
    arr = map(int,raw_input().split())
    res = get(arr,m,n)
    print min(res)+1,max(res)+1

