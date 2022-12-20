lst = list(map(int,input().split()))
a = max(lst)
b = min(lst)
if a%2 == 0 or b%2 == 0:
    print(0)
else:
    print(b)