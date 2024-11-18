n = int(input())
lst = list(map(list,input()))
ans = 0
for i in range(n):
    ans += int(lst[i][0])
print(ans)