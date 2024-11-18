n = list(input())
while n[-1] == '0':
    n.pop()
print(n.count('0'))