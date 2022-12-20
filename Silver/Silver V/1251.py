word = input()
voca = []

for i in range(len(word)-2):
    for j in range(i+1, len(word)-1):
        for k in range(j+1, len(word)):
            temp = word[:j][::-1] + word[j:k][::-1] + word[k:][::-1]
            voca.append(temp)
print(min(voca))