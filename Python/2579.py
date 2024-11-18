n = int(input())
stair = [int(input()) for i in range(n)]
dp = [0]*n

if n < 3:
    print(sum(stair))
else:
    dp[0] = stair[0]
    dp[1] = sum(stair[0:2])
    for i in range(2,n):
        dp[i] = max(dp[i-2]+stair[i],dp[i-3]+stair[i-1]+stair[i])
    print(dp[-1])