from collections import deque

n = int(input())

graph = [list(map(int, ' '.join(input().split()))) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        global count # global 변수에 유의하기
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

count = 0
result = 0
num = []
# main
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            num.append(count)
            result += 1
            count = 0

num.sort()

print(result)
for i in range(len(num)):
    print(num[i])


