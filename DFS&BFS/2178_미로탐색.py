n, m = map(int, input().split())

path = []
for _ in range(n):
    row = list(map(int, input().split('')))
    path.append(row)

result = set()
def backtrack(i, j):
    result.add((i, j))
    path[i][j] = 0
    if i == n and j == m:
        return len(result)
    if (i >= n or j >= m or i < 0 or j < 0
        or (path[i+1][j] == 0 and path[i-1][j] == 0
    and path[i][j+1] == 0 and path[i][j-1] == 0)):
        result.remove((i,j))

    rep = (backtrack(i+1, j) or
           backtrack(i-1, j) or
           backtrack(i, j+1) or
           backtrack(i, j-1))

backtrack(1, 1)


# BFS 는 언제나 최단 경로를 보장한다
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [list(map(int, ' '.join(input().split()))) for _ in range(n)]

queue = deque([(0,0)])

dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 0

#BFS
while queue:
    x, y = queue.popleft()
    for i in range(4):
        next_x, next_y = x + dx[i], y + dy[i]
        if 0<= next_x < n and 0 <= next_y < m:
            if graph[next_x][next_y] == 1:
                queue.append((next_x, next_y))
                graph[next_x][next_y] = graph[x][y] + 1
print(graph[n-1][m-1])
