first_list = []
second_list = []

n,m = map(int,input().split())

for i in range(n):
    first_list.append(list(map(int,input().split())))
for i in range(n):
    second_list.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        print(first_list[i][j] + second_list[i][j], end=' ')
    print()