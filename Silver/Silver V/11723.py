import sys
n = int(sys.stdin.readline())
set_arr = set([])

for i in range(n):
    cmd = sys.stdin.readline().split()
    if len(cmd) == 2:
        x = int(cmd[1])
        f = cmd[0]
        if f == 'add':
            set_arr.add(x)
        if f == 'remove':
            set_arr.discard(x)
        if f == 'check':
            if x in set_arr:
                print(1)
            else:
                print(0)
        if f == 'toggle':
            if x in set_arr:
                set_arr.discard(x)
            else:
                set_arr.add(x)
    else:
        f = cmd[0]
        if f == 'all':
            set_arr = set([x for x in range(1,21)])
        if f == 'empty':
            set_arr = set()