test_case = int(input())
for x in range(test_case):
    n = int(input())
    for i in range(n):
        a,b = map(int,input().split())
        print(a+b, a*b)