# 입력 받기
n, m, v = map(int, input().split())
graph = [[False]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = True

visited1 = [False]*(n+1)
visited2 = visited1.copy()

# dfs 구현
def dfs(v):
    visited1[v] = True
    print(v, end=' ')
    for i in range(1, n+1):
        if graph[v][i] == True and visited1[i] == False:
            dfs(i)

#bfs 구현
def bfs(v):
    queue = [v]
    visited2[v] = True
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in range(1, n+1):
            if visited2[i] == False and graph[v][i] == True:
                queue.append(i)
                visited2[i] = True

dfs(v)
print()
bfs(v)





