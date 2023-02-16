a = input()
k = 0
while True:
    try:
        print(a[k], end='')
        k += ord(a[k])-64
    except:
        break