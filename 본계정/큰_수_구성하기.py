import sys
input = sys.stdin.readline
from itertools import product

n,k = map(int,input().split())
lst = sorted(list(map(str,input().split())), reverse=True)
t = len(str(n))
ans = -1

while True:
    for i in (list(product(lst, repeat=t))):
        if int(''.join(i)) <= n:
            ans = max(ans, int(''.join(i)))
    if ans != -1:
        break
    else:
        t -= 1

print(ans)