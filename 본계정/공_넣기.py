import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = [0 for _ in range(n)]

for p in range(m):
    i,j,k = map(int,input().split())
    for q in range(i,j+1):
        lst[q-1] = k

lst = list(map(str, lst))

print(' '.join(lst))