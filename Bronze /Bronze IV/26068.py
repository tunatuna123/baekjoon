n = int(input())
ans = 0
for i in range(n):
    a = int(input().removeprefix('D-'))
    if a <= 90:
        ans += 1
print(ans)