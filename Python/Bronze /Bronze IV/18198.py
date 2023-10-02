a,b = 0,0
k = input()

while True:
    if a >= 11 and a-b >=2:
        print("A")
        break
    elif b >= 11 and b-a >=2:
        print("B")
        break
    else:
        if k[0] == 'A':
            a += int(k[1])
            k = k[2:]
        elif k[0] == 'B':
            b += int(k[1])
            k = k[2:]