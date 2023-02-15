m,s,g = map(float,input().split())
a,b = map(float,input().split())
l,r = map(float,input().split())

k = l/a
t = r/b

lv = m/g+1 if m%g else m/g
rv = m/s+1 if m%s else m/s

if lv+k < rv+t:
    print('friskus')
else:
    print('latmask')