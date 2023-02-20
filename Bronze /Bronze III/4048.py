def ans(lst):
    return [abs(lst[0]-lst[1]),abs(lst[2]-lst[1]),abs(lst[3]-lst[2]),abs(lst[0]-lst[3])]
while True:
    arr = list(map(int,input().split()))
    if arr == [0,0,0,0]:
        break
    for i in range(1,max(arr)):
        if 2**i >= max(arr):
            break
    for _ in range(3*i+1):
        if arr == [0,0,0,0]:
            print(_-1)
            break
        arr = ans(arr)