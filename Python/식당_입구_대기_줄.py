import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
std = deque([])
ans = [0,100001]

for i in range(n):
    cmd = list(map(int,input().split()))
    if cmd[0] == 1:
        std.append(cmd[1])
        if ans[0] < len(std):
            ans = [len(std),std[-1]]
        elif ans[0] == len(std):
            if std[-1] < ans[1]:
                ans = [len(std),std[-1]]
    else:
        std.popleft()
        if ans[0] < len(std):
            ans = [len(std),std[-1]]
        elif ans[0] == len(std):
            if std[-1] < ans[1]:
                ans = [len(std),std[-1]]

print(' '.join(map(str,ans)))