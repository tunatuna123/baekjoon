n = int(input())
for i in range(n):
    t = None
    a = input()
    for j in a:
        if t != j:
            print(j, end='')
            t = j
    print()