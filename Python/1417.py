n = int(input())
dasom = int(input())
candidates = []
count = 0

for i in range(n-1):
    candidates.append(int(input()))
candidates.sort(reverse=True)

if n == 1:
    print(0)

else:
    while candidates[0] >= dasom:
        candidates[0] -= 1
        dasom += 1
        count += 1
        candidates.sort(reverse=True)

    print(count)