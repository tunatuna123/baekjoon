w = list(input())
for i in range(len(w)):
    if w[i] == 'a':
        w[i] = '4'
    elif w[i] == 'e':
        w[i] = '3'
    elif w[i] == 'i':
        w[i] = '1'
    elif w[i] == 'o':
        w[i] = '0'
    elif w[i] == 's':
        w[i] = '5'
    else:
        pass
print(''.join(w))