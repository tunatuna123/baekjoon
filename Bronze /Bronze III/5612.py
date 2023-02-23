n = int(input())
car = [int(input())]
for i in range(n):
    if car[-1] < 0:
        print(0)
        break
    a,b = map(int,input().split())
    car.append(car[-1]+a-b)
if car[-1] >= 0:
    print(max(car))