from sys import stdin
input = stdin.readline

n = int(input())
lst = []

def new_round(a):
    if a - int(a) >= 0.5:
        return int(a) + 1
    else:
        return int(a)

if n == 0:
    print(0)
else:
    for i in range(n):
        lst.append(int(input()))
    cut = new_round(n * (15/100))
    lst = sorted(lst)[cut:n-cut]
    print(new_round(sum(lst)/(len(lst))))