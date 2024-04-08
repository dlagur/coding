n = int(input())
m = int(input())

coms = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    coms[a].append(b)
    coms[b].append(a)

def dfs(v):
    if not visited[v]:
        visited[v] = True
        for i in coms[v]:
            dfs(i)

visited = [False]*(n+1)
dfs(1)
print(sum(visited)-1)
