# output : 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수
# input : 그림
# 구역의 개수가 output이므로, 구역의 모든 영역을 확인 후 count 해줘야 함 --> dfs
import sys
sys.setrecursionlimit(1000000)  # RecursionError 방지


def dfs(x, y):
    visited[x][y] = 1  # 영역 방문처리
    color = graph[x][y]  # 현재 영역의 색상

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < n) and (0 <= ny < n) and not visited[nx][ny]:
            # 같은 색상인 영역만 확인하기 위함
            if graph[nx][ny] == color:
                dfs(nx, ny)


# main
n = int(input())

graph = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

output_rg, output = 0, 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 적록색약이 없을 때의 영역 개수
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            output += 1

visited = [[0] * n for _ in range(n)]

# 적록색약: R --> G 로 변경
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

# 적록색약인 경우의 영역 개수 count
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            output_rg += 1

print(output, output_rg)
