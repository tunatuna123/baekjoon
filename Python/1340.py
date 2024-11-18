month,d,y,t = input().split()
d = int(d.removesuffix(','))
y = int(y)
h,m = map(int,t.split(':'))
month_lst = ["January" , "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
day_lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if y%400 == 0 or (y%4 == 0 and y%100 != 0):
    day_lst[1] += 1
total = sum(day_lst)*24*60

lm = month_lst.index(month)
now = (sum(day_lst[:lm])+d-1)*24*60+(h*60)+m
print(now/total*100)