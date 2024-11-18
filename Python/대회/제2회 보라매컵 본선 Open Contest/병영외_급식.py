import sys
input = sys.stdin.readline

n,x = map(int,input().split())
total = sum(list(map(int,input().split())))

if total % x != 0:
    print(0)
else:
    print(1)