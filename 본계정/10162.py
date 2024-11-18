a,b,c = 300,60,10
t = int(input())

if t%10 != 0:
    print(-1)
else:
    print(t//a, end=' ')
    t %= a
    print(t//b, end=' ')
    t %= b
    print(t//c)