ans = 0
n = int(input())
word = input()
ans += word.count('a')
ans += word.count('e')
ans += word.count('i')
ans += word.count('o')
ans += word.count('u')
print(ans)