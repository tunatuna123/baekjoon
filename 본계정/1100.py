board = []
for i in range(8):
    board.append(list(input()))

ans = 0

for i in range(8):
    for j in range(8):
        if (i+j)%2 == 0 and board[i][j] == 'F':
            ans += 1
print(ans)