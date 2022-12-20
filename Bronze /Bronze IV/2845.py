l,p = map(int,input().split())
lst = list(map(int,input().split()))

for i in lst:
    print(i-(l*p), end=' ')