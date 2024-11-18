n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    if a == 1:
        print(a,b)
        print(b)
    else:
        print(a,b)
        print((a*b)-2*(a-1))