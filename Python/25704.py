n = int(input())
m = int(input())
ans = [m]
if n >= 5:
    ans.append(m-500)
if n >= 10:
    ans.append(m*0.9)
if n >= 15:
    ans.append(m-2000)
if n >= 20:
    ans.append(m*0.75)

if int(min(ans)) < 0:
    print(0)
else:
    print(int(min(ans)))