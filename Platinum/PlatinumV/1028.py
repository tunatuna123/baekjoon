h,w = map(int,input().split())
arr = []
start = []
one_count = 0
ans = 0
for i in range(h):
    arr.append(input())

def find_start(lst,h,w):
    for i in range(h-1):
        for j in range(1,w-1):
            if lst[i][j] == '1':
                if lst[i+1][j-1] == '1' and lst[i+1][j+1] == '1':
                    start.append([i+1,j-1])

for i in range(h):
    if '1' in arr[i]:
        one_count += 1

if one_count == 0:
    print(0)
else:
    find_start(arr,h,w)
    if len(start) == 0:
        print(1)
    else:
        print(start)
        seek(arr)