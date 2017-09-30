# Enter your code here. Read input from STDIN. Print output to STDOUT

def explore(i,j,arr,visited,cc,n,m):
    count = 1
    visited[i][j] = True
    if i+1 < n and not visited[i+1][j] and arr[i+1][j] == 1:
        count += explore(i+1,j,arr,visited,cc,n,m)
    if j+1 < m and not visited[i][j+1] and arr[i][j+1] == 1:
        count += explore(i,j+1,arr,visited,cc,n,m)
    if i-1 >= 0 and not visited[i-1][j] and arr[i-1][j] == 1:
        count += explore(i-1,j,arr,visited,cc,n,m)
    if j-1 >=0 and not visited[i][j-1] and arr[i][j-1] == 1:
        count += explore(i,j-1,arr,visited,cc,n,m)
    if i-1 >= 0 and j-1 >=0 and not visited[i-1][j-1] and arr[i-1][j-1] == 1:
        count += explore(i-1,j-1,arr,visited,cc,n,m)
    if i-1 >= 0 and j+1 < m and not visited[i-1][j+1] and arr[i-1][j+1] == 1:
        count += explore(i-1,j+1,arr,visited,cc,n,m)
    if i+1 < n and j-1 >=0 and not visited[i+1][j-1] and arr[i+1][j-1] == 1:
        count += explore(i+1,j-1,arr,visited,cc,n,m)
    if i+1 <n and j+1 <m and not visited[i+1][j+1] and arr[i+1][j+1] == 1:
        count += explore(i+1,j+1,arr,visited,cc,n,m)
    cc[0] = max(cc[0],count)
    return count








def dfs(arr,n,m):
    visited = [[False for _ in range(m)] for _ in range(n)]
    cc= [-1]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and arr[i][j] == 1:
                explore(i,j,arr,visited,cc,n,m)
    return cc[0]

n = int(raw_input())
m = int(raw_input())
arr = []
for i in range(n):
    curr = map(int,raw_input().split())
    arr.append(curr)
print dfs(arr,n,m)


