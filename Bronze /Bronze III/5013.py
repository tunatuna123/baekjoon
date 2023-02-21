n = int(input())
ans = 0
for i in range(n):
    w = input()
    if 'CD' not in w:
        ans += 1
print(ans)