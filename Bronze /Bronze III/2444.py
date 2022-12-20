def up(n):
    for i in range(n-1):
        print(" "*(n-i-1), end='')
        print("*"*(2*i+1))

def down(n):
    for i in range(n):
        print(" "*i, end='')
        print("*"*(2*(n-i)-1))

n = int(input())
up(n)
down(n)