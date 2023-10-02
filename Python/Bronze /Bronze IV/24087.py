from math import ceil
s = int(input())
a = int(input())
b = int(input())

if s-a > 0:
    print(ceil((s-a)/b)*100+250)
else:
    print(250)