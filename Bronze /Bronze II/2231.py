n = int(input())
ans = []
for i in range(n):
    if (i + sum(list(map(int,str(i))))) == n:
        ans.append(i)

if not ans:
    print(0)
else:
    print(ans[0])