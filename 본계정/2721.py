n = int(input())
def t(n):
    return (n*(n+1))//2
for i in range(n):
    num = int(input())
    ans = 0
    for i in range(1,num+1):
        ans += i*t(i+1)
    print(ans)