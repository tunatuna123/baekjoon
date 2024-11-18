arr = list(map(int,input().split()))
arr.sort()
ans = []
for i in range(3):
    for j in range(3):
        ans.append(arr[i]-arr[j])
ans.append(arr[2]-(arr[0]+arr[1]))

if ans.count(0) > 3:
    print('S')
else:
    print('N')