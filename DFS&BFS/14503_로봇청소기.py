# output: 청소하는 영역의 개수
# N * M
# 동서남북
# 반시계 방향으로 90도 회전

# dfs
def dfs(x, y, d):
    global count
    # 방향 : 북 / 동 / 남 / 서
    # direction = [0, 1, 2, 3]
    if graph[x][y] == 0:
        count += 1
        graph[x][y] =2

    for _ in range(4):
        # 90도씩 왼쪽으로 회전하면서 청소할 곳이 있는지 확인
        nd = (d + 3) % 4
        nx, ny = x + dx[nd], y + dy[nd]
        if graph[nx][ny] == 0:
            # 청소
            dfs(nx, ny, nd)
            return
        d = nd

    # 청소되지 않은 빈 칸이 없는 경우
    nd = (d + 2) % 4
    nx, ny = x + dx[nd], y + dy[nd]
    # 후진 할 수 없으면 멈춤
    # 테두리는 모두 벽으로 둘러싸여 있으므로, 인덱스가 범위를 벗어날 경우는 고민하지 않아도 됨
    if graph[nx][ny] == 1:
        return
    dfs(nx, ny, d)

# main
n, m = map(int, input().split())

start_x, start_y, d = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0

dfs(start_x, start_y, d)

print(count)
