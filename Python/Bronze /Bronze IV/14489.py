a,b = map(int,input().split())
c = int(input())

if c*2 > a+b:
    print(a+b)
else:
    print((a+b)-(c*2))