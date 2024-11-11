import heapq

def solution(scoville, K):
    # 최소 힙을 이용한 구현
    min_heap = []
    for sco in scoville:
        heapq.heappush(min_heap, sco)
    
    result = 0
    
    while min_heap[0] < K:
        if len(min_heap) == 1:
            return -1
        
        # 가장 맵지 않은 음식의 스코빌 지수 + 두 번째로 맵지 않은 음식의 스코빌 지수*2
        one = heapq.heappop(min_heap)
        two = heapq.heappop(min_heap)
                    
        standard = one + two*2
        result += 1
        
        heapq.heappush(min_heap, standard)
        
        

    return result