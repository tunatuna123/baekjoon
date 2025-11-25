import sys
p,k = map(int,sys.stdin.readline().split())
o = 0
for j in range(2,k+1):
        if p % j == 0:
            print(j)
            o += j
            break
if o > k:
    sys.stdout.write("GOOD")
else:
    print("BAD",o)