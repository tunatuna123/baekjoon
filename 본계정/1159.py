n = int(input())
lst = {}
for _ in range(n):
    name = input()[0]
    if name not in lst.keys():
        lst[name] = 1
    else:
        lst[name] += 1

first = [k for k,v in lst.items() if v >= 5]
if len(first) > 0:
    print(''.join(sorted(first)))
else:
    print("PREDAJA")