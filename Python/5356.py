n = int(input())
alpha_lst = [chr(x+65) for x in range(26)]
for _ in range(n):
    num,alpha = input().split()
    num = int(num)
    for i in range(num):
        print(alpha_lst[(ord(alpha)+i-65)%26]*(i+1))
    if _ != n-1:
        print()