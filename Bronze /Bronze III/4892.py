i = 0
while True:
    n = int(input())
    if n == 0:
        break
    i += 1
    if n%2 == 0:
        print("{}. even {}".format(i,n//2))
    else:
        print("{}. odd {}".format(i,n//2))