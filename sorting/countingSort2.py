# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
arr = map(int,raw_input().split())
count = [0]*100
for x in arr:
    count[x] += 1
for i in range(100):
    if count[i] != 0:
        print " ".join(map(str,[i]*count[i])),
