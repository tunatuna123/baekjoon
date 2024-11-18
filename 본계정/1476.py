e,s,m = map(int,input().split())
e = e%15
s = s%28
m = m%19
k = 1
while True:
    if k%15 == e and k%28 == s and k%19 == m:
        print(k)
        break
    k+=1