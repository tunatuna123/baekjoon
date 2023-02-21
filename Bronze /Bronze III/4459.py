n = int(input())
dic = {}
for i in range(1,n+1):
    dic[i] = input()
k = int(input())
for i in range(k):
    num = int(input())
    if num in range(1,n+1):
        print('Rule {}: {}'.format(num,dic[num]))
    else:
        print('Rule {}: No such rule'.format(num))