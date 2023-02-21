n = int(input())
g = [1,2,3,3,4,10]
s = [1,2,2,2,3,5,10]
for _ in range(n):
    g_arr = list(map(int,input().split()))
    s_arr = list(map(int,input().split()))
    gandalf = 0
    sauron = 0
    for i in range(len(g_arr)):
        if g_arr[i] != 0:
            gandalf += g[i]*g_arr[i]
    for i in range(len(s_arr)):
        if s_arr[i] != 0:
            sauron += s[i]*s_arr[i]
    if gandalf < sauron:
        print("Battle {}: Evil eradicates all trace of Good".format(_+1))
    elif gandalf > sauron:
        print("Battle {}: Good triumphs over Evil".format(_+1))
    else:
        print("Battle {}: No victor on this battle field".format(_+1))