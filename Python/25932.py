n = int(input())
for i in range(n):
    arr = list(map(int,input().split()))
    m = arr.count(18)
    z = arr.count(17)
    if m+z == 0:
        print(' '.join(map(str,arr)))
        print('none')
    elif m+z == 1:
        if m == 1:
            print(' '.join(map(str,arr)))
            print('mack')
        else:
            print(' '.join(map(str,arr)))
            print('zack')
    else:
        print(' '.join(map(str,arr)))
        print('both')
    if i != n-1:
        print()