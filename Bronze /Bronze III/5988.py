import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    if int(input())%2 == 0:
        print('even')
    else:
        print('odd')