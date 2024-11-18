n = int(input())
ans = []
for i in range(n):
    a,d,g = map(int,input().split())
    if a == d+g:
        ans.append(a*(d+g)*2)
    else:
        ans.append(a*(d+g))
print(max(ans))