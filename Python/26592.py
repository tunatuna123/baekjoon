n = int(input())
for i in range(n):
    a,b = map(float,input().split())
    print('The height of the triangle is {:.2f} units'.format(2*a/b))