n = int(input())
ans = (25+(n*(1/100)))
if ans >= 2000:
    print('2000.00')
elif ans <= 100:
    print('100.00')
else:
    print('{:.2f}'.format(ans))