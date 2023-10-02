from collections import deque
n,m = map(int,input().split())
target = list(map(int,input().split()))
arr = deque([x+1 for x in range(n)])
ans = 0

for i in target:
    index = arr.index(i)
    if 2*index < len(arr):
        while True:
            front = arr.popleft()
            if front == i:
                break
            else:
                arr.append(front)
                ans += 1
    else:
        while True:
            if arr[0] == i:
                del arr[0]
                break
            else:
                end = arr.pop()
                ans += 1
                arr.insert(0,end)

print(ans)