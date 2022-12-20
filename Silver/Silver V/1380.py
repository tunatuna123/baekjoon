t = 0
while True:
    n = int(input())
    if n == 0:
        break

    t += 1
    students = []
    in_out_list = [0]*n
    for i in range(n):
        students.append(input())
    for i in range((2*n)-1):
        a,b = input().split()
        in_out_list[int(a)-1] += 1
    print(str(t), students[in_out_list.index(1)])
