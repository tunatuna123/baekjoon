n,m = map(int,input().split())
ans = n-7
if ans <= 0:
    ans = m+7
print(ans)