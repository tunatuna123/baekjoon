n = int(input())
for i in range(1,2*n):
    print("*"*min(i,2*n-i), end='')
    print(" "*((2*n)-(min(i,2*n-i)*2)), end='')
    print("*"*min(i,2*n-i))