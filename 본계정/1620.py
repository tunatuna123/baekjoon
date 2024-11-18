import sys
n,m = map(int,sys.stdin.readline().split())
poke = {}
quiz = []

for i in range(n):
    a = sys.stdin.readline().rstrip('\n')
    poke[a] = i
    poke[i] = a

for i in range(m):
    a = sys.stdin.readline().rstrip('\n')
    if a.isdigit():
        print(poke[int(a)-1])
    else:
        print(poke[a]+1)