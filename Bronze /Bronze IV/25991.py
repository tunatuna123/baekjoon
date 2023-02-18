n = int(input())
arr = map(float,input().split())
total = 0
for i in arr:
    total += i**3
print(total**(1/3))