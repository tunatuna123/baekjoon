a = int(input())
b = int(input())
c = int(input())

if a+b+c != 180:
    print("Error")
else:
    if a==b==c==60:
        print("Equilateral")
    elif a==c or b==c or c==a:
        print("Isosceles")
    else:
        print("Scalene")