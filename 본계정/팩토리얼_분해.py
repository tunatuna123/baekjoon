import sys
input = sys.stdin.readline
from math import factorial

n = int(input())

if n == 0:
    print('NO')
    sys.exit(0)

for i in range(20, -1, -1):
    k = factorial(i)
    if k <= n:
        n -= k

if n == 0:
    print('YES')
else:
    print('NO')