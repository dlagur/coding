# 출발 지점이 정해져있고, 도착 지점 또한 정해져 있다
# 경우의 수
## s -> a, s -> b
## s -> x -> a, s -> x -> b

## -> 다익스트라 알고리즘 혹은 플로이드 워셜 알고리즘 사용

import sys, heapq

def solution(n, s, a, b, fares):
    INF = sys.maxsize

    # 문제에서 주어진 fares를 인접리스트 형태로 바꿈
    maps = [[] for _ in range(n+1)]
    for v, u, c in fares:
        maps[v].append((u, c))
        maps[u].append((v, c))

    # 다익스트라 알고리즘으로 구현
    def dijkstra(start):
        distance = [INF]*(n+1)
        distance[start] = 0
        q = [(0, start)]

        while q:
            cur_dist, cur_node = heapq.heappop(q)
            
            if distance[cur_node] < cur_dist:
                continue

            for next_node, next_dist in maps[cur_node]:
                if distance[next_node] > cur_dist + next_dist:
                    distance[next_node] = cur_dist + next_dist
                    heapq.heappush(q, (cur_dist + next_dist, next_node))
        return distance

    # i th 노드에서 시작해서 모든 정점으로 도착하는 최단거리 구하기
    D = [0] + [dijkstra(i) for i in range(1, n+1)]

    path = INF
    for i in range(1, n+1):
        path = min(path, D[s][i] + D[i][a] + D[i][b])
    
    return path