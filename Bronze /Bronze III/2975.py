while True:
    a,f,b = input().split()
    if (a,b) == ('0','0'):
        break
    if f == 'W':
        if int(a)-int(b) >= -200:
            print(int(a)-int(b))
        else:
            print('Not allowed')
    else:
        print(int(a)+int(b))