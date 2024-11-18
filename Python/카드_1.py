import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

lst = deque(range(1, n+1))
ans = list()

while len(lst) >= 2:
    ans.append(lst.popleft())
    lst.append(lst.popleft())

for i in (ans+list(lst)):
    print(i, end=' ')