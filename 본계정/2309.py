lst = []
for i in range(9):
    lst.append(int(input()))

for i in range(9):
    for j in range(9):
        if i != j:
            total = 0
            ans = []
            for k in range(9):
                if k != i and k != j:
                    total += lst[k]
                    ans.append(lst[k])
            if total == 100:
                for k in sorted(ans):
                    print(k)