# recursion == 10**6 일 때 메로리 초과

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

Flag = False


def dfs(x, y):
    move = graph[x][y]
    dx = [0, move]
    dy = [move, 0]
    global Flag
    for i in range(2):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < n) and (0 <= ny < n):
            if graph[nx][ny] == -1:
                Flag = True
                return
            else:
                dfs(nx, ny)


dfs(0, 0)

if Flag:
    print("HaruHaru")
else:
    print("Hing")
