n = int(input())
arr = []
for i in range(n):
    a,n = input().split()
    arr.append((int(a),n))
arr.sort(key= lambda x : x[0])
for i in arr:
    print(i[0],i[1])