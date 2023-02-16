t1,m1,t2,m2 = map(int,input().split())
if t1*60+m1 > t2*60+m2:
    print(24*60-(t1*60+m1)+t2*60+m2, (24*60-(t1*60+m1)+t2*60+m2)//30)
else:
    print(-(t1*60+m1)+(t2*60+m2),(-(t1*60+m1)+(t2*60+m2))//30)