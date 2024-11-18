n = int(input())
for i in range(n):
    p,t = map(int,input().split())
    p += t//4
    p -= t//7
    print(p)