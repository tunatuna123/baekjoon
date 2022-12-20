while True:
    ans = 0
    n = input()
    if n == '0':
        break
    else:
        for i in n:
            if i == "0":
                ans += 4
            elif i == '1':
                ans += 2
            else:
                ans += 3
        ans += len(n)+1
        print(ans)