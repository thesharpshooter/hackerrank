# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(raw_input())
a = map(int,raw_input().split())
m = int(raw_input())
b = map(int,raw_input().split())
c = Counter(b)
for x in a:
    c[x] -= 1
print " ".join(map(str,sorted(list(c.elements()))))
