n = int(input())
print('int a;')
print('int *ptr = &a;')
if n >= 2:
    print('int **ptr2 = &ptr;')
for i in range(n-2):
    print('int '+'*'*(i+3)+'ptr'+str(i+3)+' = &ptr'+str(i+2)+';')