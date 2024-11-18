n = input()

a = n.split('0')
while '' in a:
    a.remove('')
a = len(a)

b = n.split('1')
while '' in b:
    b.remove('')
b = len(b)

print(min(a,b))