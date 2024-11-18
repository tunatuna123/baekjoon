n = input()
cnt = [0] * 9
for i in n:
    k = int(i)
    if k == 9:
        k = 6
    cnt[k] += 1
cnt[6] = (cnt[6]+1) // 2
print(max(cnt))