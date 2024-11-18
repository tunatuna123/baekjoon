import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int,input().split()))

coord = sorted(list(set(x)))
ans = {coord[i]:i for i in range(len(coord))}

for i in x:
    print(ans[i],end=' ')