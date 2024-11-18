dic = {}
num = sorted(list(map(int,input().split())))
for i in range(3):
    dic[chr(i+65)] = num[i]
arr = list(input())
for i in range(3):
    print(dic[arr[i]],end='')
    if i != 2:
        print(' ', end='')