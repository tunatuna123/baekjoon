import sys
input = sys.stdin.readline
from math import sqrt

n = int(input())
monitor = []

for i in range(1,n+1):
    w,h = map(int,input().split())
    monitor.append([i, sqrt(h**2+w**2)/77])

monitor.sort(key=lambda x: (-x[1], x[0]))

for i in monitor:
    print(i[0])