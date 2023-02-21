while True:
    tri = sorted(list(map(int,input().split())))
    if tri == [0,0,0]:
        break
    if tri[2] >= tri[0]+tri[1]:
        print('Invalid')
    else:
        tri = set(tri)
        if len(tri) == 1:
            print('Equilateral')
        elif len(tri) == 2:
            print('Isosceles')
        else:
            print('Scalene')