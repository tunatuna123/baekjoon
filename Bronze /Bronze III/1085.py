x,y,w,h = map(int,input().split())
dis = [x,y,w-x,h-y]
print(min(dis))