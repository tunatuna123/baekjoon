from collections import deque

n,k = map(int,input().split())
visitied = list(0 for i in range(100001))

def bfs():
    q = deque([n])
    while q:
        num = q.popleft()
        if num == k:
            print(visitied[num])
            break
        for i in [num-1,num+1,num*2]:
            if (100000 >= i >= 0) and (not visitied[i]):
                visitied[i] = visitied[num] + 1
                q.append(i)

bfs()