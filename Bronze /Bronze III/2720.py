n = int(input())
for i in range(n):
    change = int(input())
    print(change // 25, end=' ')
    change %= 25
    print(change // 10, end=' ')
    change %= 10
    print(change // 5, end=' ')
    change %= 5
    print(change)
