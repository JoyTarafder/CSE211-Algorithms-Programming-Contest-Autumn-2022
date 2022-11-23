ar_count = int(input())
arr = list(map(int, input().rstrip().split()))

c = 0
temp = arr[0]
for i in range(1,len(arr)):
    if arr[i] > temp:
        temp = arr[i]
for i in range(0,len(arr)):
    if arr[i] == temp:
        c = c + 1
print(c)