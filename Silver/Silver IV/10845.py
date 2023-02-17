import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque([])

for i in range(n):
    a = sys.stdin.readline().split()
    if len(a) == 2:
        queue.append(a[1])
    else:
        a = a[0]
        if a == 'front':
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif a == 'back':
            if queue:
                print(queue[-1])
            else:
                print(-1)
        elif a == 'pop':
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif a == 'size':
            print(len(queue))
        elif a == 'empty':
            if queue:
                print(0)
            else:
                print(1)