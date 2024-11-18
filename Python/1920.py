n = int(input())
n_lst = sorted(list(map(int,input().split())))
m = int(input())
m_lst = list(map(int,input().split()))

def binary_search(target):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start+end)//2
        if n_lst[mid] == target:
            return True
        elif n_lst[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

for i in m_lst:
    if binary_search(i):
        print(1)
    else:
        print(0)