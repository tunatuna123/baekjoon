import sys
from collections import deque
input = sys.stdin.readline

n,m,p = map(int,input().split())
stage = []

for i in range(n):
    stage.append(list(map(int,input().split())))

for i in stage:
    if -1 in i:
        items = i.count(-1)
        current_stage = deque(sorted(i)[items:])
        for j in list(current_stage):
            if p >= j:
                p += j
            elif p < j and p*2 > j and items > 0:
                items -= 1
                p *= 2
                p += j
            else:
                print(0)
                sys.exit(0)
    else:
        current_stage = deque(sorted(i)[items:])
        for j in list(current_stage):
            if p >= j:
                p += j
            else:
                print(0)
                sys.exit(0)

print(1)