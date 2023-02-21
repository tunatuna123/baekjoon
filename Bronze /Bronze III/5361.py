cost = [350.34,230.90,190.55,125.30,180.90]
n = int(input())
for i in range(n):
    arr = list(map(int,input().split()))
    ans = 0
    for i in range(5):
        ans += cost[i]*arr[i]
    print('${:.2f}'.format(ans))