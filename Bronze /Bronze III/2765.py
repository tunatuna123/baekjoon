pi = 3.141592
i = 1
while True:
    r,n,t = map(float, input().split())
    if n==0:
        break
    else:
        distance = pi*(r/(12*5280))*n