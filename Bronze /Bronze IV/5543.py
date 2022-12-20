buger = []
soda = []
for i in range(3):
    buger.append(int(input()))
for i in range(2):
    soda.append(int(input()))
print(min(buger)+min(soda)-50)