n = int(input())
room = []
flip_room = [[0]*n for x in range(n)]
w = 0
h = 0

for i in range(n):
    room.append(input())

for i in range(n):
    for j in range(n):
        flip_room[j][i] = room[i][j]

for i in range(n):
    flip_room[i] = ''.join(flip_room[i])

for i in room:
    for j in i.split('X'):
        if len(j) >= 2:
            w += 1

for i in flip_room:
    for j in i.split('X'):
        if len(j) >= 2:
            h += 1
print(w,h)