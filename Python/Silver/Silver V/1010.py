from math import factorial


n = int(input())
for i in range(n):
    n,m = map(int,input().split())
    print(int(factorial(m)/(factorial(n)*factorial(m-n))))