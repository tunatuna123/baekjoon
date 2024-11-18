import sys
input = sys.stdin.readline

name = input().strip()
n = int(input())
lst = []
for i in range(n):
    lst.append(input().strip())
lst.sort()

score = []
for i in range(n):
    L = name.count('L') + lst[i].count('L')
    O = name.count('O') + lst[i].count('O')
    V = name.count('V') + lst[i].count('V')
    E = name.count('E') + lst[i].count('E')
    score.append(((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100 )

print(lst[score.index(max(score))])