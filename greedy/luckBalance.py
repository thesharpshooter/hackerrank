# Enter your code here. Read input from STDIN. Print output to STDOUT
n,k = map(int,raw_input().split())
res = []
count = 0
for i in range(n):
    a,b = map(int,raw_input().split())
    if b :
        res.append(a)
    else:
        count += a
res= sorted(res)
if k == 0:
    print count - sum(res)
else:
    print count + sum(res[-k:]) - sum(res[:-k])
