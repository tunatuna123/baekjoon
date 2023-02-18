g,p,t = map(int,input().split())
every = g*p
if (g+(t*p)) > every:
    print(1)
elif (g+(t*p)) < every:
    print(2)
else:
    print(0)