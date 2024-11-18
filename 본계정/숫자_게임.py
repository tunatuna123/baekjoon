import sys
input = sys.stdin.readline

from itertools import combinations

t = int(input())
ans = []

for _ in range(t):
    k = 0
    for i in combinations(list(map(int,input().split())), 3):
        k = max(k,sum(i)%10)
    ans.append(k)

ans.reverse()
print(t-ans.index(max(ans)))