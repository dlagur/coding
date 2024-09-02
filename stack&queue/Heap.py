# 힙을 저장하는 표준적인 자료구조는 배열
# 구현을 쉽게 하기 위해 배열의 첫 번째 인덱스인 0은 사용하지 않음
# 특정 위치의 노드 번호는 새로운 노드가 추가되어도 변하지 않음
# 루트 노드의 오른쪽 노드 번호는 항상 3

## 왼쪽 자식의 인덱스 = 부모의 인덱스*2
## 오른쪽 자식의 인덱스 = 부모의 인덱스*2 + 1
## 부모의 인덱스 = 자식의 인덱스 / 2

# heap 구현
numbers = [10, 20, 50]
heap = [0 for _ in range(len(numbers)+1)]

for number in numbers:
    heap.append(number)
    current_index = len(heap)-1 # 삽입한 원소의 인덱스

    # 힙 조건을 유지하기 위해 위로 올리기
    while current_index > 1 and heap[current_index] > heap[current_index // 2]:
        # 부모와 자식 노드를 교환
        heap[current_index], heap[current_index // 2] = heap[current_index // 2], heap[current_index]
        current_index = current_index // 2

print(heap)


# heapq 모듈을 이용한 heap 구현
import heapq

heap = []
heapq.heappush(heap, 50)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)

print(heap) # [10, 50, 20]
