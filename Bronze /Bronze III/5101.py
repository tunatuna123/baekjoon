while True:
    a,b,c = map(int,input().split())
    if (a,b,c) == (0,0,0):
        break
    if (c-a)%b == 0 and c >= a:
        print((c-a)//b+1)
    else:
        print('X')