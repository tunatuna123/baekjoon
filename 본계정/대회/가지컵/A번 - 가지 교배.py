n = int(input())
gaji = input().split()
m,k = map(int,input().split())
josu_gaji = []

for i in range(m):
    arr = list(map(int,input().split()))
    lst = []
    for j in range(k):
        lst.append(gaji[arr[j]-1])
    if 'P' in lst:
        josu_gaji.append('P')
    else:
        josu_gaji.append('W')

if 'W' in josu_gaji:
    print('W')
else:
    print('P')
