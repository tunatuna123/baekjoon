from collections import deque
stack = deque([x for x in range(1,int(input())+1)])

while len(stack) != 1:
    stack.popleft()
    stack.append(stack.popleft())
print(stack[0])