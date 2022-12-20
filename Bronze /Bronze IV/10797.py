n = int(input())
car = list(map(int,input().split()))
total = 0

for i in car:
    if i == n:
        total += 1

print(total)