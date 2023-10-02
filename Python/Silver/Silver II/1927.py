from heapq import heappop,heappush
import sys

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    a = int(sys.stdin.readline())
    if a == 0:
        try:
            print(heappop(heap))
        except:
            print(0)
    else:
        heappush(heap,a)