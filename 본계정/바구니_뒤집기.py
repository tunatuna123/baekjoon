import sys
input = sys.stdin.readline

n,m = map(int,input().split())

lst = [_ for _ in range(1,n+1)]

for p in range(m):
    i,j = map(int,input().split())
    for q in range(i-1,j):
        lst[q] = lst[n-q]