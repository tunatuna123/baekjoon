import sys
h,w,b = map(int,sys.stdin.readline().split())
floor = []
for i in range(h):
    floor.append(list(map(int,sys.stdin.readline().rstrip().split())))
time = (1e9)

for i in range(257):
    use = 0
    take = 0
    for y in range(h):
        for x in range(w):
            if floor[y][x] > i:
                take += floor[y][x] - i
            else:
                use += i - floor[y][x]
    if use > take + b:
        continue
    if 2*take + use <= time:
        time = 2*take + use
        ans = i
print(time,ans)