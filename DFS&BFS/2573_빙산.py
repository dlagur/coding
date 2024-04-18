from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
day = 0
check = False # Flag 설정

def bfs(a, b):
    q.append((a, b))
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<= nx < n) and (0 <= ny < m):
                if graph[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif graph[nx][ny] == 0:
                    count[x][y] += 1 # 상하좌우로 둘러싼 빙산의 양
    return 1

while True:
    visited = [[False]*m for _ in range(n)]
    count = [[0]*m for _ in range(n)] # 누적되어 빼야 하는 빙산의 양을 저장하기 위함
    result = []
    # BFS 수행 과정
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:
                result.append(bfs(i, j))

    ## 여기서 갈렸는데,,,
    for i in range(n):
        for j in range(m):
            graph[i][j] -= count[i][j]
            if graph[i][j] < 0: # 빙산이 0보다 작아지면 0으로 처리
                graph[i][j] = 0

    if len(result) == 0: # 빙산이 다 없어졌을 때
        break
    if len(result) >= 2:
        check = True # 빙산 분리
        break
    day += 1 # while 문 돌때마다 day 추가

if check:
    print(day)
else:
    print(0)

