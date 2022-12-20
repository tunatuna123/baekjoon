arr = []
count = 0
n,m = 4,5
arr = [[0,1,2,3,4], [5,6,7,8,9], [10,11,12,13,14], [15,16,17,18,19]]

for p in range(n-2):
    for q in range(m-2):
        for i in range(len(arr)-3):
            for j in range(len(arr)-3):
                print([row[i+q:i+3+q] for row in arr[j+p:j+3+p]])