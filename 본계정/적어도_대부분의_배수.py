lst = list(map(int,input().split()))
ans = 1
ans_lst = []

while True:
    cnt = 0
    for i in lst:
        if ans%i == 0:
            cnt += 1
    if cnt >= 3:
        print(ans)
        break
    else:
        ans += 1