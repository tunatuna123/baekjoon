first = '9780921418'
for i in range(3):
    first += input()

total = 0
for i in range(len(first)):
    total += int(first[i]) * (((i%2)*2)+1)

print("The 1-3-sum is", str(total))