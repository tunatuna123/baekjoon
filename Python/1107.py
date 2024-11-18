import sys
target = int(sys.stdin.readline())
n = int(sys.stdin.readline())
broken = list(map(int,sys.stdin.readline().split()))
ans = abs(target-100)

for i in range(1000001):
    num = str(i)
    for j in range(len(num)):
        if int(num[j]) in broken:
            break
        elif j == len(num)-1:
            ans = min(ans,abs(int(num)-target)+len(num))

print(ans)