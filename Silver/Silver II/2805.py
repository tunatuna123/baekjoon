n,m = map(int,input().split())
wood = list(map(int,input().split()))
start,end = 0,max(wood)

while start <= end:
    mid = (start+end)//2
    tree = 0
    for i in wood:
        if i > mid:
            tree += i - mid
    if tree >= m:
        start = mid+1
    else:
        end = mid-1
print(end)