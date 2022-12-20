month = input()
day = input().zfill(2)

if int(month+day) < 218:
    print("Before")
elif int(month+day) > 218:
    print("After")
else:
    print("Special")