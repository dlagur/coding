import heapq

def dijkstra(graph, start):
    # 각 노드까지의 최단 거리를 저장하는 테이블
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # 시작 노드의 거리는 0으로 초기화

    # 우선순위 큐(최소 힙) 생성
    priority_queue = [(0, start)]  # (거리, 노드)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # 이미 처리된 노드는 무시 (이전에 더 짧은 경로로 처리된 경우)
        if current_distance > distances[current_node]:
            continue

        # 현재 노드와 연결된 다른 인접 노드들을 확인
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # 계산된 거리가 현재 저장된 거리보다 짧으면 업데이트
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# 그래프 예시 (인접 리스트)
graph = {
    1: [(2, 2), (3, 5), (4, 1)],
    2: [(1, 2), (3, 3), (4, 2)],
    3: [(1, 5), (2, 3), (4, 3), (5, 1)],
    4: [(1, 1), (2, 2), (3, 3), (5, 1)],
    5: [(3, 1), (4, 1)]
}

# 시작 노드
start_node = 1

# 다익스트라 실행
shortest_distances = dijkstra(graph, start_node)

# 결과 출력
for node, distance in shortest_distances.items():
    print(f"Node {node}: {distance}")
