import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
queue = deque()

def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[z][x][y] + 1
                    queue.append((nz, nx, ny))

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append((i,j,k))

bfs()

# 완전히 익을 수 없는 조건

flag = False
day = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                flag = True
            day = max(day, graph[i][j][k])

if flag:
    print(-1)
else:
    print(day-1)
