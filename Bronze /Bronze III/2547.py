n = int(input())
for i in range(n):
    input()
    k = int(input())
    lst = [int(input()) for j in range(k)]
    if sum(lst)%k == 0:
        print("YES")
    else:
        print("NO")