N = int(input())
F = int(input())
answer = 0

N //= 100
N *= 100

while (N + answer) % F != 0 and answer < 100:
    answer += 1

print(format(answer, '02'))