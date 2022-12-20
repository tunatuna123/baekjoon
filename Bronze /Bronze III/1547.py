def swap(arr,a,b):
    arr[a-1],arr[b-1] = arr[b-1],arr[a-1]

lst = [1,2,3]

n = int(input())
for i in range(n):
    p,q = map(int,input().split())
    swap(lst,p,q)

print(lst.index(1)+1)