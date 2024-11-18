n = int(input())
group = [1,3,5]
for i in range(n):
    g,c,e = map(int,input().split())
    ans = (e-c)*group[g-1]
    if ans <= 0:
        print(0)
    else:
        print(ans)