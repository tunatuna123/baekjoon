a = int(input())
b = int(input())
ans = (a+b)%12
if ans == 0:
    print(12)
else:
    print(ans)