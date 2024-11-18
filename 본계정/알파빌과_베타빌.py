import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = list(map(int,input().split()))
friend = list(map(int,input().split()))

ans = 0

for i in range(m):
    if lst[i] not in friend:
        ans += 1

print(ans)