n = int(input())
a = n%8
if a == 0:
    a = 8
    n -= 8
print(chr(a+96)+str(n//8+1))