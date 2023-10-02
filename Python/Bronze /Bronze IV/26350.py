n = int(input())
for i in range(n):
    arr = list(map(int,input().split()))
    num = arr[0]
    coins = arr[1:]
    print('Denominations:', ' '.join(map(str,coins)))
    a = coins[0]
    for j in coins[1:]:
        if j >= a*2:
            a = j
        else:
            print('Bad coin denominations!')
            break
    if a == coins[-1]:
        print('Good coin denominations!')
    if i != n-1:
        print()