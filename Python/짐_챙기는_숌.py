import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
books = deque(map(int,input().split()))
temp = 0
ans = 1

if n == 0:
    print(0)
    sys.exit(0)

while books:
    if temp + books[0] <= m:
        temp += books.popleft()
    else:
        temp = 0
        ans += 1

print(ans)