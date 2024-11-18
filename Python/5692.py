from math import factorial
while True:
    a = input()
    if a == '0':
        break
    ans = 0
    for i in range(1,len(a)+1):
        ans += int(a[len(a)-i])*factorial(i)
    print(ans)