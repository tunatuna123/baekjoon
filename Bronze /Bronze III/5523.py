import sys
input = sys.stdin.readline
n = int(input())
a_ans = 0
b_ans = 0
for i in range(n):
    a,b = map(int,input().split())
    if a>b:
        a_ans += 1
    elif b>a:
        b_ans += 1
print(a_ans,b_ans)