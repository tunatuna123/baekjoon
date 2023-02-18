n = int(input())
for i in range(n):
    ans = 0
    t = int(input())
    for j in range(t):
        a,c,m = input().split()
        ans += int(c)*float(m)
    print('${:.2f}'.format(ans))