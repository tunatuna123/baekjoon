h,m,s = map(int,input().split())
s += int(input())
m += s//60
s %= 60
h += m//60
m %= 60
h %= 24
print(h,end=" ")
print(m,end=" ")
print(s)