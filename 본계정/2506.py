n = int(input())
ans = 0
lst = input().replace(' ', '')
for i in lst.split('0'):
    if i != '':
        ans += (len(i)*(len(i)+1))//2
print(ans)