people = 0
lst = []
for i in range(10):
    a,b = map(int,input().split())
    people += b
    people -= a
    lst.append(people)

print(max(lst))