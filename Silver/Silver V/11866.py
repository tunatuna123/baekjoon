from collections import deque
n,k = map(int,input().split())
stack = deque([x for x in range(1,n+1)])
ans = []
while stack:
    for i in range(k-1):
        stack.append(stack[0])
        stack.popleft()
    ans.append(str(stack.popleft()))
print('<', end='')
print(', '.join(ans), end='')
print('>')