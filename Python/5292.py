n = int(input())
for i in range(1,n+1):
    if i%15 == 0:
        print('DeadMan')
    elif i%3 == 0:
        print('Dead')
    elif i%5 == 0:
        print('Man')
    else:
        print(i,end='')
        if i != n:
            print(' ',end='')