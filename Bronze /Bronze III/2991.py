a,b,c,d = map(int,input().split())
arr = list(map(int,input().split()))

for i in arr:
    ans = 0
    if a >= i%(a+b) > 0:
        ans += 1
    if c >= i%(c+d) > 0:
        ans += 1
    print(ans)