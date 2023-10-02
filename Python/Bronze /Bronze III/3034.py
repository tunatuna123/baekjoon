from math import sqrt
n,w,h = map(int,input().split())
for i in range(n):
    a = int(input())
    if a > sqrt(h**2+w**2):
        print('NE')
    else:
        print('DA')