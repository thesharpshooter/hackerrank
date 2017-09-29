# Enter your code here. Read input from STDIN. Print output to STDOUT
def countSwap(a,b):
    count = 0
    n = len(a)
    pos = {}
    for i in range(n):
        pos[b[i]] = i
    for i in range(n):
        if i != pos[a[i]]:
            nex = pos[a[i]]
            pos[b[i]] = nex
            pos[b[nex]] = i
            b[i],b[nex] = b[nex],b[i]
            count += 1
    return count
n = int(raw_input())
arr = map(int,raw_input().split())
sor = sorted(arr)
sor2 = sor[::-1]
print min(countSwap(sor,arr[:]),countSwap(sor2,arr[:]))
