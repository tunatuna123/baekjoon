n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    a = bin(a).count('1')
    if (a+int(b))%2 == 0:
        print('Valid')
    else:
        print('Corrupt')