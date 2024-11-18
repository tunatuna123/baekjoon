from collections import deque

n = int(input())
tower = deque(map(int,input().split()))

a = tower.popleft()
ans = 1

while tower:
    if tower[0] < a:
        if len(tower) > 1 and tower[0] == tower[1]:
            tower.popleft()
            a = tower.popleft()
            ans += 1
        else:
            tower.popleft()
    else:
        a = tower.popleft()
        ans += 1
print(ans)