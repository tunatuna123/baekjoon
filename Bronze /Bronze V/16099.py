n = int(input())
for i in range(n):
    lt,wt,le,we = map(int,input().split())
    if le*we == lt*wt:
        print("Tie")
    else:
        print("Eurecom" if le*we > lt*wt else "TelecomParisTech")