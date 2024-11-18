import sys
input = sys.stdin.readline

t = int(input())
lst = []
dic = {}
cnt = 0

for _ in range(t):
    lst.append(list(map(int,input().split())))

lst.sort(key=lambda x: x[2], reverse=True)

for i in range(t):
    if cnt == 3:
        break
    if lst[i][0] not in dic.keys():
        dic[lst[i][0]] = 1
        print(" ".join(list(map(str,lst[i][:2]))))
        cnt += 1
    else:
        if dic[lst[i][0]] < 2:
            dic[lst[i][0]] += 1
            print(" ".join(list(map(str,lst[i][:2]))))
            cnt += 1