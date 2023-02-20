cnt = 0
for i in range(5):
    if 'FBI' in input():
        print(i+1)
        cnt += 1
if cnt == 0:
    print("HE GOT AWAY!")