lst = []
odd = []
for i in range(7):
    lst.append(int(input()))

for i in range(7):
    if lst[i]%2 == 1:
        odd.append(lst[i])

if len(odd) != 0:
    print(sum(odd))
    print(min(odd))
else:
    print(-1)