import sys
input = sys.stdin.readline

n = int(input())
lst = sorted(list(map(int,input().split())))

if n%2 == 1:
    print(lst[int((n-1)/2)]**2)
else:
    print(lst[0]*lst[-1])