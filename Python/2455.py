people = 0
lst = []
for i in range(4):
    a,b = map(int,input().split())
    people += b
    people -= a
    lst.append(people)

print(max(lst))