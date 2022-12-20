p1,s1 = map(int,input().split())
p2,s2 = map(int,input().split())

a = p1+s2
b = p2+s1

if a > b:
    print("Persepolis")
elif a < b:
    print("Esteghlal")
else:
    if s1 > s2:
        print("Esteghlal")
    elif s1 < s2:
        print("Persepolis")
    else:
        print("Penalty")