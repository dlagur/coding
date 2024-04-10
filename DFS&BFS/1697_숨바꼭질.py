from collections import deque

n, k = map(int, input().split())

graph = [0] * 100001

graph[n] = 0


# 1초 후에 X-1 / X+1 / 순간이동 --> 2*X
def bfs(n):
    queue = deque()
    queue.append(n)

    global count
    while queue:
        v = queue.popleft()
        if v == k:
            print(graph[v])
            break
        for nv in (v - 1, v + 1, 2 * v):
            if 0 <= nv <= 100000 and not graph[nv]:
                graph[nv] = graph[v] + 1
                queue.append(nv)


bfs(n)
