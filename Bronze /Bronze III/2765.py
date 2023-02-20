pi = 3.141592
i = 1
while True:
    r,n,t = map(float, input().split())
    if n==0:
        break
    else:
        distance = pi*(r/(12*5280))*n
        mph = distance/(t/3600)
        print('Trip #{}: {:.2f} {:.2f}'.format(i,distance,mph))
        i += 1