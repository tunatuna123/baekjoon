while True:
    arr = list(map(int,input().split()))
    if arr[0] == 0:
        break
    ans = 1
    for i in range(1,len(arr),2):
        ans = ans*arr[i]-arr[i+1]
    print(ans)