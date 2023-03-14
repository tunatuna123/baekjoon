import re
p = re.compile('(100+1+|01)+')
n = int(input())
for i in range(n):
    a = input()
    if p.fullmatch(a):
        print('YES')
    else:
        print('NO')