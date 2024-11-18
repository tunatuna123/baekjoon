import sys
input = sys.stdin.readline
from itertools import permutations

x,y = map(int,input().split())
people = []
ans = []

def dist(a,b,c,d):
    return ((a-c)**2 + (b-d)**2)**(1/2)

for i in range(3):
    people.append(list(map(int,input().split())))

for i in list(permutations(people, r=3)):
    dis = 0
    a,b = x,y
    for j in i:
        dis += dist(a,b,j[0],j[1])
        a,b = j[0],j[1]
    ans.append(dis)

print(int(min(ans)))