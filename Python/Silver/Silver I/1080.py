h,w = map(int,input().split())
arr_a = []
arr_b = []
ans = 0

for i in range(h):
    arr_a.append(list(map(int,input())))
for i in range(h):
    arr_b.append(list(map(int,input())))

def flip(p,q):
    for x in range(p,p+3):
        for y in range(q,q+3):
            if arr_a[x][y] == 0:
                arr_a[x][y] = 1
            else:
                arr_a[x][y] = 0

if (h<3 or w<3) and (arr_a != arr_b):
    print(-1)
else:
    for i in range(h-2):
        for j in range(w-2):
            if arr_a[i][j] != arr_b[i][j]:
                flip(i,j)
                ans += 1
    if arr_a != arr_b:
        print(-1)
    else:
        print(ans)