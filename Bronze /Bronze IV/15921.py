n = int(input())
if n == 0:
    print("divide by zero")
    quit()
lst = list(map(int,input().split()))

mean = sum(lst)/n
ex = 0
for i in set(lst):
    ex += i*(lst.count(i)/n)
if ex == 0:
    print("divide by zero")
    quit()
print("%.2f"%(mean/ex))