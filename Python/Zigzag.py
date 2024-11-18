n = int(input())
lst = list(map(int,input().split()))

k = 2
ans = 2
for i in range(n-2):
    if lst[i] <= lst[i+1] and lst[i+1] <= lst[i+2]:
        k = 2
    elif lst[i] >= lst[i+1] and lst[i+1] >= lst[i+2]:
        k = 2
    else:
        k += 1
    ans = max(ans, k)

print(ans)