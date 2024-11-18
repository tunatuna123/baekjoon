import sys
input = sys.stdin.readline

num = input().strip()
print(oct(int(num, 2)).removeprefix('0o'))