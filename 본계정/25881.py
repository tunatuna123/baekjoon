r,t = map(int,input().split())
n = int(input())
for i in range(n):
    a = int(input())
    if a <= 1000:
        print(a,a*r)
    else:
        print(a,(1000*r)+((a-1000)*t))