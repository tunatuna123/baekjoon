import sys
n,m = map(int,sys.stdin.readline().split())
no_hear = set()
no_see = set()

for i in range(n):
    no_hear.add(sys.stdin.readline().rstrip('\n'))

for i in range(m):
    no_see.add(sys.stdin.readline().rstrip('\n'))

print(len(no_hear.intersection(no_see)))
for i in sorted(no_hear.intersection(no_see)):
    print(i)