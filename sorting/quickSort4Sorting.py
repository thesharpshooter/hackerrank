# Enter your code here. Read input from STDIN. Print output to STDOUT
c = 0
def insertion(arr,n):
    count = 0
    for i in range(1,n):
        p = arr[i]
        j = i-1
        while j >= 0 and arr[j] > p:
            arr[j+1] = arr[j]
            count += 1
            j -= 1
        arr[j+1] = p
    return count

def quick(arr):
    global c
    n = len(arr)
    if n <= 1:
        return arr
    p = arr[-1]
    l = -1
    for i in range(n-1):
        if arr[i] < p:
            l += 1
            arr[i],arr[l] = arr[l],arr[i]
            c += 1
    arr[l+1],arr[-1] = arr[-1],arr[l+1]
    c += 1
    return quick(arr[:l+1])+[arr[l+1]] + quick(arr[l+2:])

n = int(raw_input())
arr = map(int,raw_input().split())
c1 = insertion(arr[:],n)
quick(arr[:])
print c1 - c

















