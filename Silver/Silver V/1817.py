n,m = map(int,input().split())
books = list(map(int,input().split()))

total = 0
ans = 1
for i in books:
    if total+i <= m:
        total += i
    else:
        total = 0
        ans += 1

print(ans)