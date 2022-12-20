first_team = list(map(int,input().split()))
second_team = list(map(int,input().split()))

def ans(lst):
    return lst[0]*6 + lst[1]*3 + lst[2]*2 + lst[3]*1 + lst[4]*2

print(ans(first_team),ans(second_team))