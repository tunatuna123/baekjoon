n = int(input())
time = []
ans = 0

for i in range(n):
    time.append(tuple(map(int,input().split())))
time.sort(key=lambda x: (x[1],x[0]))
ke = 0

for start,end in time:
    if start >= ke:
        ans += 1
        ke = end

print(ans)