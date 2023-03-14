while True:
    k = 0
    t = 2
    a = float(input())
    if a == 0:
        break
    while True:
        if k >= a:
            print(t-2,'card(s)')
            break
        k += 1/t
        t += 1