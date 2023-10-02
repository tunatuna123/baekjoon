k,n = map(int,input().split())
wire = []
for i in range(k):
    wire.append(int(input()))
start,end = 1,max(wire)
while start <= end:
    mid = (start+end)//2
    ans = 0
    for i in wire:
        ans += i//mid
    if ans >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)