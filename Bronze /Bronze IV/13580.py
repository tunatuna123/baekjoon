lst = list(map(int,input().split()))
lst.sort(reverse=True)
if len(set(lst)) == 2:
    print("S")
elif lst[0] == lst[1]+lst[2]:
    print("S")
else:
    print("N") 