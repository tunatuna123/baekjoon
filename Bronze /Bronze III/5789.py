n = int(input())
for i in range(n):
    w = input()
    if w[len(w)//2] == w[len(w)//2-1]:
        print('Do-it')
    else:
        print('Do-it-Not')