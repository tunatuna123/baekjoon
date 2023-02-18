n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
for i in range(n):
    print(int(m*(arr[i]/sum(arr))))