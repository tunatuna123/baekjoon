t = 1
while True:
    arr = list(map(int,input().split()))
    if arr[0] == 0:
        break
    else:
        n = arr[0]
        arr = arr[1:]
        if n%2 == 1:
            print("Case "+str(t)+': '+'{:.1f}'.format(arr[(n-1)//2]))
            t += 1
        else:
            print("Case "+str(t)+': '+'{:.1f}'.format((arr[n//2]+arr[n//2-1])/2))
            t += 1