from collections import deque

n,q = map(int,input().split())
query = deque(map(int,list(input())))

for _ in range(q):
    command = deque(map(int,input().split()))
    if command.popleft() == 1:
        query[command.popleft()] = command.pop()
        print(query)