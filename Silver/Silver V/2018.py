n = int(input())
ans,s,start,end = 0,0,0,0

while end <= n:
    if s < n:
        end += 1
        s += end
    elif s > n:
        start += 1
        s -= start
    else:
        ans += 1
        end += 1
        s += end
print(ans)