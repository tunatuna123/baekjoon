yut = {1:'A', 2:'B', 3:'C', 4:'D', 0:'E'}
for _ in range(3):
    lst = list(map(int,input().split()))
    print(yut[lst.count(0)])