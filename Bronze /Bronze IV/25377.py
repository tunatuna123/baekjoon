n = int(input())
ans = []
for i in range(n):
    a,b = map(int,input().split())
    if a <= b:
        ans.append(b)
try:
    print(min(ans))
except:
    print(-1)