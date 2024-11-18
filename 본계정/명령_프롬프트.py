import sys
input = sys.stdin.readline

n = int(input())
commands = []

for i in range(n):
    commands.append(input())

if n == 1:
    print(commands[0])
    sys.exit(0)
else:
    ans = []
    for i in range(len(commands[0])):
        words = set()
        for j in range(n):
            words.add(commands[j][i])
        if len(words) > 1:
            ans.append('?')
        else:
            ans.append(list(words)[0])

print(''.join(ans))