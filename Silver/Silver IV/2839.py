n = int(input())
ans = 0
while n:
    if 0 < n < 3:
        print(-1)
        break
    else:
        if n % 5 == 0:
            ans += n//5
            print(ans)
            break
        n -= 3
        ans += 1
else:
    print(ans)