w = int(input())
l = int(input())
h = int(input())
if max(w,l)/min(w,l) <= 2 and min(w,l)/h >= 2:
    print('good')
else:
    print('bad')