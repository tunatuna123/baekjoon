n = int(input())
for i in range(n):
    alpha = [chr(i+65) for i in range(26)]
    arr = list(input())
    ans = 0
    for i in alpha:
        if i not in arr:
            ans += ord(i)
    print(ans)