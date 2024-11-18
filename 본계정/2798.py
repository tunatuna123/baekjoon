n,t = map(int,input().split())
arr = list(map(int,input().split()))
ans = 0
for i in range(n-2):
    for j in range(i+1,n):
        for k in range(j+1,n):
            s = arr[i]+arr[j]+arr[k]
            if s <= t:
                ans = max(ans,s)
print(ans)