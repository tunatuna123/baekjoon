n,m = map(int,input().split())
arr = []
ans = []

def check_white(k):
    count_w = 0
    for i in range(8):
        for j in range(8):
            if (i+j)%2 == 0:
                if k[i][j] != 'W':
                    count_w += 1
            else:
                if k[i][j] != 'B':
                    count_w += 1
    return count_w

def check_black(k):
    count_b = 0
    for i in range(8):
        for j in range(8):
            if (i+j)%2 == 0:
                if k[i][j] != 'B':
                    count_b += 1
            else:
                if k[i][j] != 'W':
                    count_b += 1
    return count_b

for i in range(n):
    arr.append(list(input()))

for p in range(n-7):
    for q in range(m-7):
        for i in range(len(arr)-8):
            for j in range(len(arr)-8):
                print([row[i+q:i+8+q] for row in arr[j+p:j+8+p]])
                ans.append(check_white([row[i+q:i+8+q] for row in arr[j+p:j+8+p]]))
                ans.append(check_black([row[i+q:i+8+q] for row in arr[j+p:j+8+p]]))

print(ans)
