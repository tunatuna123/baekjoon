x,y = map(int,input().split())
ans = (1000/y)*x
n = int(input())
arr = []
for i in range(n):
    a,b = map(int,input().split())
    ans = min(ans,(1000/b)*a)
print(ans)