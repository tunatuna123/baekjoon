n = int(input())
a = 1
while True:
    if a*(a+1)//2 > n:
        print(a-1)
        break
    elif a*(a+1)//2 == n: 
        print(a)
        break
    a += 1