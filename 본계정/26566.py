from math import pi
n = int(input())
for i in range(n):
    a1,p1 = map(int,input().split())
    r1,p2 = map(int,input().split())
    wp = p1/a1
    sp = p2/(pi*(r1**2))
    if wp > sp:
        print('Whole pizza')
    else:
        print('Slice of pizza')