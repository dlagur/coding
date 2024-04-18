import sys
sys.setrecursionlimit(100000)

# 상, 하, 좌, 우
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, h):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if (0 <= nx < n) and (0 <= ny < n) and not sink_graph[nx][ny] and graph[nx][ny] > h:
           sink_graph[nx][ny] = True
           dfs(nx, ny, h)

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans = 1
for k in range(max(map(max, graph))):
    sink_graph = [[False]*n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and not sink_graph[i][j]:
                count += 1
                sink_graph[i][j] = True
                dfs(i,j,k)
        ans = max(ans, count)

print(ans)
