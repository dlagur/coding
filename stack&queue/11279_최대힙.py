n = int(input())

heap = [0]
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(heap) == 1:
            print(0)
        else:
            print(heap[1])
            heap[1], heap[-1] = heap[-1], heap[1]
            heap = heap[:-1]
    else:
        heap.append(x)
    current_index = len(heap) - 1

    while current_index > 1 and heap[current_index] > heap[current_index // 2]:
        heap[current_index], heap[current_index // 2] = heap[current_index // 2], heap[current_index]
        current_index = current_index // 2


import sys
import heapq as hq

n = int(input())
heap = []
for i in range(n):
    x = int(sys.stdin.readline())
    # 입력 값이 0이 아니면 해당 값을 heap에 push
    # heapq 모듈에 정의되어 있는 heappush(heap, value)
    # (-value, value)로 구성된 튜플을 만들어 heappush 함수의 인자로 주게 되면 튜플의 0번째 원소인 -value를 기준으로 heap을 구성
    # 기존의 value가 가장 클수록 -value의 값이 가장 작은 값이 되어 루트 노드에 올 수 있음(heapq는 최소 힙을 지원하기 때문)
    if x:
        hq.heappush(heap, (-x, x))
    else:
        if len(heap) >= 1:
            print(hq.heappop(heap)[1])
        else:
            print(0)
