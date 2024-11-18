from collections import deque
import sys
n = int(sys.stdin.readline())
stack = deque([])
for i in range(n):
    a = sys.stdin.readline().split()
    if len(a) == 2:
        if a[0] == 'push':
            stack.append(a[1])
    else:
        a = a[0]
        if a == 'top':
            if stack:
                print(stack[-1])
            else:
                print(-1)
        elif a == 'size':
            print(len(stack))
        elif a == 'empty':
            if stack:
                print(0)
            else:
                print(1)
        elif a == 'pop':
            if stack:
                print(stack.pop())
            else:
                print(-1)