# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/python
def merge(a,b):
    global answer
    i = 0
    j = 0
    na = len(a)
    nb = len(b)
    res = [0]*(na+nb)
    k = 0
    while i < na and j<nb:
        if a[i] <= b[j]:
            res[k] = a[i]
            i += 1
            k += 1
        else:
            res[k] = b[j]
            k += 1
            answer += na-i
            j += 1
    for _ in range(i,na):
        res[k] = a[_]
        k += 1
    for _ in range(j,nb):
        res[k] = b[_]
        k += 1
    return res
def dnc(a):
    n = len(a)
    if n <= 1:
        return a
    l = dnc(a[:n/2])
    r = dnc(a[n/2:])
    return merge(l,r)
n = input()
for iterate in range( n ):
    x = input()
    a = [ int( i ) for i in raw_input().strip().split() ]
    answer = 0
    a = dnc(a)
    # Write code to compute answer using x, a and answer
    print answer

