n = int(input())
k = int(input())
arr = []

for i in range(1,int(n**(1/2))+1):
    if (n/i).is_integer():
        arr.append(i)
        arr.append(int(n/i))
arr.sort()

for i in range(len(arr)):
    if arr[i] > k:
        print(i)