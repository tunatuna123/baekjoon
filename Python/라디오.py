import sys
input = sys.stdin.readline

a,b = map(int,input().split())
n = int(input())
favorites = []
sub = []

for i in range(n):
    channel = int(input())
    favorites.append(channel)
    sub.append(abs(channel-b))

sub.append(abs(a-b)-1)

print(min(sub)+1)