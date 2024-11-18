n = int(input())
people = []

for i in range(n):
    lst = list(map(int,input().split()))

    if len(set(lst)) == 1:
        people.append(10000+(lst[0]*1000))
    elif len(set(lst)) == 2:
        for i in range(2):
            if lst.count(list(set(lst))[i]) == 2:
                people.append(1000+(list((set(lst)))[i]*100))
    else:
        people.append(max(lst)*100)

print(max(people))