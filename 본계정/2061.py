a,b = map(int,input().split())
c = 0
for i in range(2,b):
    if a%i == 0:
        print("BAD {}".format(str(i)))
        c += 1
        break
if c == 0:
    print("GOOD")