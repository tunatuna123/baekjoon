n = input()
ans = 0
while len(n) > 1:
    n = str(sum(map(int,list(n))))
    ans += 1
print(ans)
if int(n)%3 == 0:
    print("YES")
else:
    print('NO')