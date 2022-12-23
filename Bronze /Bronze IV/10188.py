n = int(input())
for i in range(3):
    a,b = map(int,input().split())
    if a <= 20 or b <= 20:
        for i in range(b):
            print("X"*a)
    print()