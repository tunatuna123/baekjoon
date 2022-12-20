lst = []
for i in range(5):
    lst.append(int(input()))

if lst[0] < 0:
    print(-lst[0]*lst[2]+lst[3]+lst[1]*lst[4])
else:
    print((lst[1]-lst[0])*lst[4])