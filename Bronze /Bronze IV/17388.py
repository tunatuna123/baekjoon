school = ['Soongsil', 'Korea', 'Hanyang']
lst = list(map(int,input().split()))
if sum(lst) >= 100:
    print("OK")
else:
    print(school[lst.index(min(lst))])