n = int(input())
for _ in range(n):
    num = int(input())
    ans = [['J']*num for x in range(num)]
    for i in range(num):
        for j in range(num):
            if i == 0 or j == 0 or i == num-1 or j == num-1:
                ans[i][j] = '#'
    for i in range(num):
        print(''.join(ans[i]))
    if _ != n-1:
        print()