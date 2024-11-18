import sys
input = sys.stdin.readline

n,a,b = map(int,input().split())

if a>b:
    print('Subway')
elif a<b:
    print('Bus')
else:
    print('Anything')