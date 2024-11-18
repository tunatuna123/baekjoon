from math import sqrt
n = int(input())
for i in range(n):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    d = sqrt((x1-x2)**2 + (y1-y2)**2)
    if d == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif d == r1+r2 or d == abs(r1-r2):
        print(1)
    elif abs(r1-r2) < d < r1+r2:
        print(2)
    else:
        print(0)