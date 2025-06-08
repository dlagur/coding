def find(parent, x):
    '''
    역할 :  x의 루트(부모)를 찾는 함수.

    경로 압축(Path Compression)을 적용하여 재귀적으로 최상단 부모 노드를
    찾고, parent[x]를 해당 루트로 갱신

    x가 자기 자신이 아닌 경우, 부모를 재귀적으로 찾아서 갱신함으로써 트리의 높이를 줄이고
    이후의 탐색 속도를 높이는 역할.
    '''
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    '''
    역할 : 두 정점 a,b 가 속한 집합을 하나로 합침

    각 정점의 루트를 찾고, 숫자가 작은 쪽을 부모로 하여 하나의 트리로 병합

    Union By Rank 를 수행하여 불필요하게 트리가 깊어지는 것을 막음
    '''
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

def minimum_cost_to_split(N, edges):
    '''
    역할 : N개의 노드와 edges 리스트를 바탕으로 두 개의 마을로 분리하기 위한
    최소 비용을 계산

    1. 초기화 : parent[i] = i로 모든 노드의 부모를 자기 자신으로 설정
    2. 간선 정렬 : 간선을 비용 기준으로 오름차순 정렬
    3. MST 구성 : 크루스칼 알고리즘을 이용하여 사이클이 생기지 않게 간선 선택 MST 구성 + 총 비용 누적
    4. 가장 비싼 간선 제거 : MST에 포함된 간선 중 가장 비싼 하나 제거 --> 가장 큰 간선을 빼서 MST를 두 개 연결 요소로 나누는 원리
    '''
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
