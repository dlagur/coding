import heapq

def solution(operations):
    min_heap = []  # 최소 힙
    max_heap = []  # 최대 힙 (음수로 저장하여 최대 힙처럼 사용)
    entry_map = {}  # 각 값의 유효 상태를 관리할 딕셔너리

    for ops in operations:
        if ops[0] == "I":  # 삽입 연산
            num = int(ops.split(' ')[-1])
            heapq.heappush(min_heap, num)  # 최소 힙에 삽입
            heapq.heappush(max_heap, -num)  # 최대 힙에 음수로 삽입
            entry_map[num] = entry_map.get(num, 0) + 1  # 삽입된 횟수 기록

        elif ops == "D -1":  # 최소값 삭제
            while min_heap and entry_map[min_heap[0]] == 0:
                heapq.heappop(min_heap)  # 유효하지 않은 값 제거
            if min_heap:
                min_val = heapq.heappop(min_heap)
                entry_map[min_val] -= 1

        elif ops == "D 1":  # 최댓값 삭제
            while max_heap and entry_map[-max_heap[0]] == 0:
                heapq.heappop(max_heap)  # 유효하지 않은 값 제거
            if max_heap:
                max_val = -heapq.heappop(max_heap)
                entry_map[max_val] -= 1

    # 마지막으로 남은 값들 동기화
    while min_heap and entry_map[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and entry_map[-max_heap[0]] == 0:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        return [-max_heap[0], min_heap[0]]  # [최댓값, 최소값]
    else:
        return [0, 0]  # 힙이 비어있는 경우 [0, 0] 반환
