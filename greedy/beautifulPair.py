# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(raw_input())
a = map(int,raw_input().split())
b = map(int,raw_input().split())
count = 0
c = Counter(b)
for x in a:
    if c[x] > 0:
        count += 1
        c[x] -= 1
if count < n:
    print count+1
else:
    print count-1

