n,k = map(int,input().split())
lst = []
for i in range(1,n+1):
    if n%i == 0:
        lst.append(i)

if k > len(lst):
    print(0)
else:
    print(lst[k-1])