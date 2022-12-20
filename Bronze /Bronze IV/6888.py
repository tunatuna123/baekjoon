x = int(input())
y = int(input())

for i in range(x,y+1):
    if (x-i) % 60 == 0:
        print("All positions change in year {}".format(i))