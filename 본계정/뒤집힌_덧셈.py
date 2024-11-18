import sys
input = sys.stdin.readline

a,b = input().split()

def rev(num):
    return int(num[::-1])

print(rev(str(rev(a) + rev(b))))