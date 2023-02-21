n = int(input())
for i in range(n):
    k = int(input())
    p1,p2 = 0,0
    for _ in range(k):
        a,b = input().split()
        if a != b:
            if (a,b) == ('R','P'):
                p2 += 1
            elif (b,a) == ('R','P'):
                p1 += 1
            elif (a,b) == ('R','S'):
                p1 += 1
            elif (b,a) == ('R','S'):
                p2 += 1
            elif (a,b) == ('P','S'):
                p2 += 1
            elif (b,a) == ('P','S'):
                p1 += 1
    if p1 > p2:
        print('Player 1')
    elif p2 > p1:
        print('Player 2')
    else:
        print('TIE')