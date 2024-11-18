from collections import Counter
lst = list(map(int,input().split()))
cnt = Counter(lst)
if len(dict(cnt)) == 2:
    for key,value in dict(cnt).items():
        if value == 1:
            print(chr(65+lst.index(key)))
else:
    print("*")