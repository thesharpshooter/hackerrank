# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
arr = map(int,raw_input().split())
count = [0]*100
for x in arr:
    count[x] += 1
for x in count:
    print x,
