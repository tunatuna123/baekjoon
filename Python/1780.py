n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int,input().split())))

minus_one = 0
zero = 0
one = 0

def split_paper(x,y,k):
    global minus_one,zero,one
    num = paper[x][y]
    for i in range(x,x+k):
        for j in range(y,y+k):
            if num != paper[i][j]:
                for p in range(3):
                    for q in range(3):
                        split_paper(x+p*(k//3),y+q*(k//3),k//3)
                return
    if num == -1:
        minus_one += 1
    elif num == 1:
        one += 1
    else:
        zero += 1

split_paper(0,0,n)
print(minus_one)
print(zero)
print(one)