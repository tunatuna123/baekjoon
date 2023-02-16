n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    if (a <= 1 and b <=2) or (a <= 2 and b <= 1):
        print('Yes')
    else:
        print('No')