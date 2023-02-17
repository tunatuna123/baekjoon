n = int(input())
ans = []
for i in range(n):
    ans.append(list(map(int,input().split())))
ans.sort()
for i in ans:
    print(i[0],i[1])