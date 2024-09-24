def bellman_ford(graph, start, n):
    # 거리 테이블을 무한대로 초기화
    distances = {node: float('inf') for node in range(1, n + 1)}
    distances[start] = 0  # 시작 노드의 거리는 0으로 설정

    # 모든 간선을 N-1번 반복하여 완화
    for _ in range(n - 1):
        for u in graph:
            for v, w in graph[u]:
                if distances[u] != float('inf') and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w

    # 음의 사이클 확인: N번째 반복에서도 값이 업데이트되면 음의 사이클이 존재
    for u in graph:
        for v, w in graph[u]:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                print("Negative weight cycle detected!")
                return None

    return distances

# 그래프 예시 (인접 리스트, 음의 가중치 포함)
graph = {
    1: [(2, 4), (3, 3)],
    2: [(4, -1)],
    3: [(2, -2), (4, 2)],
    4: []
}

# 노드의 수
n = 4

# 시작 노드
start_node = 1

# 벨만-포드 알고리즘 실행
shortest_distances = bellman_ford(graph, start_node, n)

if shortest_distances:
    # 결과 출력
    for node, distance in shortest_distances.items():
        print(f"Node {node}: {distance}")
