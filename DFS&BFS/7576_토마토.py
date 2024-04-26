from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# bfs
def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m) and not graph[nx][ny]:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

# main
m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

q = deque([])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))

# 검산 부분
bfs()
count = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    count = max(count, max(i))

print(count - 1)
