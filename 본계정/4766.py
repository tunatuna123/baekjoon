first = float(input())
while True:
    second = float(input())
    if second == 999:
        break
    print("{:.2f}".format(second-first))
    first = second