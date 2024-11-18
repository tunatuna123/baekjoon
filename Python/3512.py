n,c = map(int,input().split())
room = []
for i in range(n):
    a,b = input().split()
    room.append((int(a),b))
total_area = 0
for i in room:
    total_area += i[0]
print(total_area)
bedroom_area = 0
for i in room:
    if i[1] == 'bedroom':
        bedroom_area += i[0]
print(bedroom_area)
minus = 0
for i in room:
    if i[1] == 'balcony':
        minus += i[0]*c/2
print(total_area*c-minus)