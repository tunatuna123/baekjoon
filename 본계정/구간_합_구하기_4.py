import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = list(map(int,input().split()))

prefixsum = [0]*(n+1)
prefixsum[1] = lst[0]
for i in range(2,n+1):
    prefixsum[i] = prefixsum[i-1] + lst[i-1]

for i in range(m):
    a,b = map(int,input().split())
    print(prefixsum[b] - prefixsum[a-1])