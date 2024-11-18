a,b,c,d = map(int,input().split())
res = a/b*c/d/2
if int(res) == res:
    print(1)
else:
    print(0)