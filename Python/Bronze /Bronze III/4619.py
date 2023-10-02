while True:
    a,b = map(int,input().split())
    if (a,b) == (0,0):
        break
    ans = 0
    while ans**b < a:
        ans += 1
    print(ans if ans**b-a < a-(ans-1)**b else ans-1)