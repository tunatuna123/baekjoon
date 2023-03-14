ans = int(input())
while True:
    a = input()
    if a == '=':
        break
    if a == '+':
        ans += int(input())
    elif a == '-':
        ans -= int(input())
    elif a == '/':
        ans //= int(input())
    else:
        ans *= int(input())
print(ans)