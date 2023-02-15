data_set = int(input())

for x in range(data_set):
    ans = 0
    n,s,d = map(int,input().split())
    for i in range(n):
        vi,di = map(int,input().split())
        if vi/s <= d:
            ans += di
    print("Data Set {}:".format(x+1))
    print(ans)
    if x != data_set-1:
        print()