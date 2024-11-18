n = int(input())
for _ in range(n):
    num = int(input())
    ans = []
    for i in range(1,num+1):
        for j in range(i,num+1):
            if i+j == num and i != j:
                ans.append(str(i)+' '+str(j))
    print('Pairs for {}: '.format(num)+', '.join(ans))