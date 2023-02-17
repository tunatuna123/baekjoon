from collections import deque
n = int(input())
for i in range(n):
    ans = 0
    paper,target = map(int,input().split())
    queue = deque(list(map(int,input().split())))
    while queue:
        max_value = max(queue)
        front = queue.popleft()
        target -= 1
        if front == max_value:
            ans += 1
            if target < 0:
                print(ans)
                break
        else:
            queue.append(front)
            if target < 0:
                target = len(queue)-1