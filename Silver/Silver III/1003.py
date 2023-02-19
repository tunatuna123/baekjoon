n = int(input())
arr = [(1,0),(0,1)]
for i in range(n):
    a = int(input())
    if a >= len(arr):
        for i in range(a-len(arr)+1):
            arr.append((arr[-2][0]+arr[-1][0],arr[-2][1]+arr[-1][1]))
        print(arr[-1][0],arr[-1][1])
    else:
        print(arr[a][0],arr[a][1])