import sys
input = sys.stdin.readline

u,n = map(int,input().split())
dic = {}

for i in range(n):
    a,b = input().strip().split()
    if int(b) in dic:
        dic[int(b)].append(a)
    else:
        dic[int(b)] = [a]

dic = sorted(dic.items(), key=lambda x: x[0])

t = 100001
for i in dic:
    if len(i[1]) < t:
        t = len(i[1])
        ans = (i[1][0],i[0])

for i in ans:
    print(i, end=' ')