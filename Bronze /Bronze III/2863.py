a, b = map(int, input().split())
c, d = map(int, input().split())
arr = []
arr.append(a / c + b / d)
arr.append(c / d + a / b)
arr.append(d / b + c / a)
arr.append(b / a + d / c)
print(arr.index(max(arr)))