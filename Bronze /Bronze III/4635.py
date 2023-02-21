while True:
    n = int(input())
    if n == -1:
        break
    time = [0]
    ans = 0
    for i in range(n):
        a,b = map(int,input().split())
        ans += a*(b-time[-1])
        time.append(b)
    print("{} miles".format(ans))