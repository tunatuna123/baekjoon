lst = list(map(int,input().split()))
a = min(lst)-1
b = max(lst)-1
print(abs(((b//4)-(a//4)))+abs(((a%4)-(b%4))))