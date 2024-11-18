import sys
input = sys.stdin.readline

num = input().strip()

def mul(lst):
    ans = 1
    for i in lst:
        ans *= int(i)
    return ans

if num == '1':
    print('NO')
    sys.exit(0)

for i in range(len(num)):
    if mul(num[i:]) == mul(num[:i]):
        print('YES')
        sys.exit(0)

print('NO')