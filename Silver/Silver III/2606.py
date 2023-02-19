computer = int(input())
n = int(input())
graph = [[]*computer for x in range(computer+1)]
ans = 0
was = [0]*(computer+1)


for i in range(n):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(k):
    global ans
    was[k] = 1
    for i in graph[k]:
        if was[i] == 0:
            dfs(i)
            ans += 1

dfs(1)
print(ans)