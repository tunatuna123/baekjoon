from math import factorial
n = list(str(factorial(int(input()))))
n.reverse()
for i in range(len(n)):
    if n[i] != '0':
        print(i)
        break