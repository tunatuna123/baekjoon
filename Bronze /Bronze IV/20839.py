a,b,c = map(int,input().split())
x,y,z = map(int,input().split())

if x >= a and y >= b and z >= c:
    print('A')
elif x >= a/2 and y >= b and z >= c:
    print('B')
elif y >= b and z >= c:
    print('C')
elif y >= b/2 and z >= c:
    print('D')
else:
    print('E')