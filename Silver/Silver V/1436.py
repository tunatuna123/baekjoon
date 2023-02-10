ans = int(input())
cnt = 0
devil = 666
while True:
    if '666' in str(devil):
        cnt += 1
    if cnt == ans:
        print(devil)
        break
    else:
        devil += 1