n=int(input())
print("Gnomes:")
for i in range(n):
    lst = list(map(int,input().split()))
    if lst == sorted(lst) or lst == sorted(lst,reverse=True):
        print("Ordered")
    else:
        print("Unordered")