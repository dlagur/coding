from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# bfs --> 최소한의 필요한 지렁이 수
def bfs(x, y):
    q = deque([])
    q.append((x, y))
    graph[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m) and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 0

# main
t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())

    graph = [[0]*m for _ in range(n)]

    for _ in range(k):
        i, j = map(int, input().split())
        graph[j][i] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
                count += 1

    print(count)

# 생각하는 능력을 기르자.
# 메모리를 어떻게 하면 더 효율적으로 사용할 수 있는지,
# 시간복잡도를 어떻게 하면 더 효율적으로 작성할 수 있는지 충분히 고민해야 한다.
