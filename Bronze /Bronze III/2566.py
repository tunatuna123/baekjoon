lst = []
max_lst = []

for i in range(9):
    lst.append(list(map(int,input().split())))

for i in range(9):
    max_lst.append(max(lst[i]))
a = max_lst.index(max(max_lst))
b = lst[a].index(max(lst[a]))

print(lst[a][b])
print(a+1,b+1)