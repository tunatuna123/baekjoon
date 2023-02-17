n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))
hashmap = {}
ans = []

for i in n_list:
    if i in hashmap.keys():
        hashmap[i] += 1
    else:
        hashmap[i] = 1
for i in m_list:
    if i in hashmap:
        ans.append(str(hashmap[i]))
    else:
        ans.append('0')
print(' '.join(ans))