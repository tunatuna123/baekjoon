alpha = [chr(x+65) for x in range(26)]
arr = list(input())
for i in arr:
    if i in alpha:
        alpha.remove(i)
print(alpha[0])