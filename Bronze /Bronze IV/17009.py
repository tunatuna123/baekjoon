a,b = 0,0

for i in range(3):
    a += int(input())*(3-i)
for i in range(3):
    b += int(input())*(3-i)

if a > b:
    print("A")
elif b > a:
    print("B")
else:
    print("T")