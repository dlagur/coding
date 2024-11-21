m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(m)]
visited = [[False]*n for _ in range(m)]

dx = [0, 0, -1, -1, 1, 1, 1, -1]
dy = [-1, 1, -1, 1, -1, 1, 0, 0]

def dfs(a, b):
    stack = [(a, b)]
    visited[a][b] = True

    while stack:
        a, b = stack.pop()

        for i in range(8):
            nx, ny = a + dx[i], b + dy[i]
            if (0 <= nx < m) and (0 <= ny < n) and graph[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                stack.append((nx, ny))
        

count = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] and not visited[i][j]:
            count += 1
            dfs(i, j)

print(count)