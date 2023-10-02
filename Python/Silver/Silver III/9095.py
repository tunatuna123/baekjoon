n = int(input())
arr = [1,2,4]
for i in range(n):
    a = int(input())
    if a < len(arr)+1:
        pass
    else:
        for i in range(a-len(arr)):
            arr.append(arr[-1]+arr[-2]+arr[-3])
    print(arr[a-1])