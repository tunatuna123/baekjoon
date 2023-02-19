n,k = map(int,input().split())
coins = []
ans = 0

for i in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

for i in coins:
    if i <= k:
        ans += k//i
        k %= i

print(ans)