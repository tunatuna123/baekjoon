a,b,c = map(int,input().split())
k = 0
plus = [a+b,b+c,c+a]
times = [a*b,b*c,c*a]
for i in [a,b,c]:
    if i in plus:
        print(1)
        k += 1
        break
    elif i in times:
        print(2)
        k += 1
        break
if k == 0:
    print(3)