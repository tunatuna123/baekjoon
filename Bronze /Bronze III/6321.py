n = int(input())
for i in range(n):
    a = list(input())
    print('String #{}'.format(i+1))
    for j in range(len(a)):
        a[j] = (chr((ord(a[j])-ord('A')+1)%26+ord('A')))
    print(''.join(a))
    print()