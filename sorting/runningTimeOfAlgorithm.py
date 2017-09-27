# Enter your code here. Read input from STDIN. Print output to STDOUT
def count(arr,n):
    count_ = 0
    for i in range(1,n):
        temp = arr[i]
        j = i-1
        while j>=0 and arr[j] > temp:
            arr[j+1] = arr[j]
            count_ += 1
            j -= 1

        arr[j+1] = temp
    return count_
n = int(raw_input())
arr = map(int,raw_input().split())
print count(arr,n)
