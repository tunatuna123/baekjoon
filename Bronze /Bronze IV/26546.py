n = int(input())
for i in range(n):
    word,n,m = input().split()
    for j in range(len(word)):
        if j in range(int(n),int(m)):
            pass
        else:
            print(word[j], end='')
    print()