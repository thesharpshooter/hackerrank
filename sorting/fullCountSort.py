# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
count = {}
for i in range(n):
    a,string = raw_input().split()
    a = int(a)
    if i < n/2: string = "-"
    if a in count:
        count[a].append(string)
    else:
        count[a] = [string]
for x in sorted(count):
    print " ".join(count[x]),
