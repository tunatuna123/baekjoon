score = []
for i in range(5):
    score.append(sum(list(map(int,input().split()))))
print(score.index(max(score))+1,max(score))