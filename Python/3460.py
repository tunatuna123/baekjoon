n = int(input())
for i in range(n):
    num = str(bin(int(input())))[::-1]
    ans = []
    for i in range(len(num)):
        if num[i] == '1':
            ans.append(i)
    print(' '.join(map(str,ans)))