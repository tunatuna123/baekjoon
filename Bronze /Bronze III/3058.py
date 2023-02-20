n = int(input())
for i in range(n):
    arr = list(map(int,input().split()))
    even = []
    ans = 0
    for i in arr:
        if i %2 == 0:
            ans += i
            even.append(i)
    print(ans,min(even))