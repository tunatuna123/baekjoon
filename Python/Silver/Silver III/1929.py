from math import sqrt
m,n = map(int,input().split())

def find_prime(a):
    if a == 1:
        return False
    else:
        for i in range(2,int(sqrt(a)+1)):
            if a%i == 0:
                return False
        return True

for i in range(m,n+1):
    if find_prime(i):
        print(i)