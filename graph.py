def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

def minimum_cost_to_split(N, edges):
    parent = [i for i in range(N + 1)]
    edges.sort(key=lambda x: x[2])  # 비용 기준 정렬

    total = 0
    max_edge = 0

    for a, b, cost in edges:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            total += cost
            max_edge = cost

    return total - max_edge

# 예시 입력
N, M = 7, 12
edges = [
    (1, 2, 3),
    (1, 3, 2),
    (3, 2, 1),
    (2, 5, 2),
    (3, 4, 4),
    (7, 3, 6),
    (5, 1, 5),
    (1, 6, 2),
    (6, 4, 1),
    (6, 5, 3),
    (4, 5, 3),
    (6, 7, 4)
]

print(minimum_cost_to_split(N, edges))  # 출력: 최소 비용
