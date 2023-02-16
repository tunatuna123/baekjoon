x,l,r = map(int,input().split())
if x in range(l,r+1):
    print(x)
else:
    if abs(x-r) < abs(x-l):
        print(r)
    else:
        print(l)