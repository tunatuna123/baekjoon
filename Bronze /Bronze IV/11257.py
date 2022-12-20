n = int(input())
for i in range(n):
    a,b,c,d = map(int,input().split())
    if b<11 or c<8 or d<12 or b+c+d < 55:
        print(str(a),str(b+c+d),"FAIL")
    else:
        print(str(a),str(b+c+d),"PASS")