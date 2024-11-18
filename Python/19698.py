n,w,h,l = map(int,input().split())
total = (w//l)*(h//l)
if total <= n:
    print(total)
else:
    print(n)