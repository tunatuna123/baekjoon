n = int(input())
for i in range(n):
    x,y = map(int,input().split())
    d = y-x
    ans = 0
    while True:
        if d <= ans*(ans+1):
            break
        ans += 1

    if d <= ans**2:
        print(2*ans-1)
    else:
        print(2*ans)