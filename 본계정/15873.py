n = input()
if n[-1] == "0":
    a = int(n[-2:])
    b = int(n[:-2])
else:
    a = int(n[-1])
    b = int(n[:-1])
print(a+b)