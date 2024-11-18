def z(n,x,y):
    ans = 0
    while n > 1:
        if x >= 2**(n-1):
            ans += 2*(4**(n-1))
            x -= 2**(n-1)
        if y >= 2**(n-1):
            ans += (4**(n-1))
            y -= 2**(n-1)
        n -= 1
    ans += (y+(2*x))
    return ans
n,x,y = map(int,input().split())
print(z(n,x,y))