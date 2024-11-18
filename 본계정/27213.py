m = int(input())
n = int(input())
if m < 3 or n < 3:
    print(m*n)
else:
    print(m*n-((m-2)*(n-2)))