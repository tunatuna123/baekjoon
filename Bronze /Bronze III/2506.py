n = int(input())
lst = list(map(int,input().split()))
score = 1

for i in lst:
    ans = 0
    streak = 0
    if i == 1:
        ans += score
    else:
        