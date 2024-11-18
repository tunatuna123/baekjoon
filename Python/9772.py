while True:
    a,b = map(float,input().split())
    if a == 0 and b == 0:
        print('AXIS')
        break
    else:
        if a*b == 0:
            print("AXIS")
        elif a*b > 0:
            if a > 0:
                print('Q1')
            else:
                print('Q3')
        else:
            if a < 0:
                print('Q2')
            else:
                print('Q4')