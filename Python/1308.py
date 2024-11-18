import datetime
import re

sy,sm,sd = map(int,input().split())
ey,em,ed = map(int,input().split())

today = datetime.date(sy,sm,sd)
target_date = datetime.date(ey,em,ed)

def after_1000_years(a):
    ans = 0
    for i in range(a,a+1000):
        if i % 400 == 0:
            ans += 366
        elif i%100 == 0:
            ans += 365
        elif i % 4 == 0:
            ans += 366
        else:
            ans += 365
    return ans

d_day = target_date - today
if int(d_day.days) >= after_1000_years(sy):
    print("gg")
else:
    print(f"D-{d_day.days}")