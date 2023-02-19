n = int(input())
coord = []

for i in range(n):
    coord.append(tuple(map(int,input().split())))

coord.sort(key= lambda x : x[0])
coord.sort(key= lambda x : x[1])

for i in coord:
    print(' '.join(map(str,i)))