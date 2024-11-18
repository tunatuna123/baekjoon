import sys
input = sys.stdin.readline

n = int(input())

if n<3:
    print(4)
    sys.exit(0)

t = 1
while t**2 < n:
    t += 1

if t*(t-1) >= n:
    print((t-2)*2+(t-1)*2)
    sys.exit(0)
print((t-1)*4)