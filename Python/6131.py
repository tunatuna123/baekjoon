ans = 0
n = int(input())
for i in range(1,501):
    for j in range(1, 501):
        if i**2 == j**2 + n:
            ans += 1
print(ans)