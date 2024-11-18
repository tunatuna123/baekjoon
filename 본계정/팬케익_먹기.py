import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    input()
    a,b,c,d = map(int,input().split())
    small = min(a,b,c)
    print(a-small, b-small, c-small)
    