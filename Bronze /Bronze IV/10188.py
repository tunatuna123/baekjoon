n = int(input())
for i in range(n):
    x,y = map(int, input().split())
    for j in range(y):
        print("X"*x)
    if i != n-1:
        print()