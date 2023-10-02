a,b = map(int,input().split())
if a+b == 0:
    print("Not a moose")
else:
    if a != b:
        print("Odd", str(max(a,b)*2))
    else:
        print("Even", str(a*2))