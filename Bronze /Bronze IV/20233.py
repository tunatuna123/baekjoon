a = int(input())
x = int(input())
b = int(input())
y = int(input())
t = int(input())

if t <= 30:
    print(a, end=' ')
else:
    print(a+21*(x*(t-30)), end=' ')
if t <= 45:
    print(b)
else:
    print(b+21*(y*(t-45)))