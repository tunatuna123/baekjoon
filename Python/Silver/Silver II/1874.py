n = int(input())
ans = []
stack = []
t = 1
k = 0
for i in range(n):
    num = int(input())
    while t <= num:
        stack.append(t)
        ans.append('+')
        t += 1
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        k += 1
        break

if k == 0:
    for i in ans:
        print(i)
else:
    print('NO')