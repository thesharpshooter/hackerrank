#!/usr/bin/py
# Head ends here
def pairs(a,k):
    count = 0
    res = {}
    n = len(a)
    for i in range(n):
        res[a[i]] = i
    temp = set()
    for x in sorted(res):
        if x+k in res and (x,x+k) not in temp:
            count += 1
            temp.add((x,x+k))
    return count
# Tail starts here
if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    _a_size=a[0]
    _k=a[1]
    b = map(int, raw_input().strip().split(" "))
    print pairs(b,_k)

