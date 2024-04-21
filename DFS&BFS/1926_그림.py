# output : 그림의 개수 / 넓이가 가장 넓은 것의 넓이
# 1로 연결된 것이 한 그림.
from collections import deque

# bfs
def bfs(a, b):
    q = deque()
    q.append((a,b))

    global count
    # 1 --> 그림 1개
    sqr = 1
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m):
                if graph[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    sqr += 1
                    q.append((nx, ny))
        count = max(sqr, count)


# main
n, m = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
result = 0
count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] and not visited[i][j]:
            result += 1
            bfs(i, j)

print(result)
print(count)
