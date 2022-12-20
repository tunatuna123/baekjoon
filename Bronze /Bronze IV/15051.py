lst = []
ans = []

for i in range(3):
    lst.append(int(input()))

ans.append(lst[0]*2+lst[1])
ans.append(lst[2]*2+lst[1])
ans.append(lst[0]+lst[2])
print(min(ans)*2)