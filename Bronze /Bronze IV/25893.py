n = int(input())
for i in range(n):
    k = 0
    a,b,c = map(int,input().split())
    for i in [a,b,c]:
        if i >= 10:
            k += 1
    if k == 0:
        print(a,b,c)
        print('zilch')
    elif k == 1:
        print(a,b,c)
        print('double')
    elif k == 2:
        print(a,b,c)
        print('double-double')
    else:
        print(a,b,c)
        print('triple-double')
    if i != n-1:
        print()