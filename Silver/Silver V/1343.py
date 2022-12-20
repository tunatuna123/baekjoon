lst = list(map(str,input().split('.')))
cnt_x = 0
cnt_ans = 0
for i in range(len(lst)):
    if lst[i] != '':
        cnt_x += 1
        if (len(lst[i])%4)%2 == 0:
            cnt_ans += 1
            lst[i] = 'AAAA'*(len(lst[i])//4) + 'BB'*((len(lst[i])%4)//2)

if cnt_x != cnt_ans:
    print('-1')
else:
    print(('.').join(lst))