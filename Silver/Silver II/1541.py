a = input().split('-')
ans = sum(list(map(int,a[0].split('+'))))
for i in a[1:]:
    ans -= sum(list(map(int,i.split('+'))))
print(ans)