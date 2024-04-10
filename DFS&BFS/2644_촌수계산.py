n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False]*(n+1)

def dfs(v, count):
    global flag
    visited[v] = True
    if v == b:
        flag = True
        print(count)

    for i in graph[v]:
        if not visited[i]:
            dfs(i, count+1)
# main
flag = False
dfs(a, 0)

if not flag:
    print(-1)


