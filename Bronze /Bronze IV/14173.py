x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())

x_list = sorted([x1,x2,x3,x4])
y_list = sorted([y1,y2,y3,y4])

print(max([x_list[3]-x_list[0], y_list[3]-y_list[0]])**2)