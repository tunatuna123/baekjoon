n = int(input())

if n == 1:
    print(1)
else:
    k = (n-1)/6
    for i in range(n):
        if i*(i+1) >= 2*k:
            print(i+1)
            break