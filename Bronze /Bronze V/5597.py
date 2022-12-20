attenders = [x for x in range(1,31)]

for i in range(28):
    attenders.remove(int(input()))
for i in range(2):
    print(attenders[i])