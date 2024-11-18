t = int(input())

dic = {2:[6,2,4,8],
        3:[1,3,9,7],
        4:[6,4],
        7:[1,7,9,3],
        8:[6,8,4,2],
        9:[1,9]}

for _ in range(t):
    a,b = map(int,input().split())
    a = a%10
    if a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 0:
        print(10)
    else:
        print(dic[a][b%len(dic[a])])