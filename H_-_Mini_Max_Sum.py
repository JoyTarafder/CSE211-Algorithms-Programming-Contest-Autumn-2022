arr = list(map(int, input().split()))
ar = []

for i in range(len(arr)):
    x = arr.pop(i)
    y = sum(arr)
    arr.insert(i,x)
    ar.append(y)
    
print(min(ar),max(ar))