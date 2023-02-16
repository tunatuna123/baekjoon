n = int(input())
for i in range(n):
    d,f,p = map(float,input().split())
    print("${:.2f}".format(d*f*p))