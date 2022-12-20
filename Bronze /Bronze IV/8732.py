lst = list(map(int,input().split()))
lst.sort(reverse=True)

if len(set(lst)) == 1:
    print(2)
elif lst[0]**2 == (lst[1]**2)+(lst[2]**2):
    print(1)
else:
    print(0)