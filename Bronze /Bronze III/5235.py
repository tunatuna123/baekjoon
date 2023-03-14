n = int(input())
for _ in range(n):
    e = 0
    o = 0
    arr = list(map(int,input().split()))
    for i in arr[1:]:
        if i%2 == 0:
            e += i
        else:
            o += i
    if e > o:
        print('EVEN')
    elif e < o:
        print('ODD')
    else:
        print('TIE')