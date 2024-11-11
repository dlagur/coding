from collections import Counter

def solution(n, works):
    
    # 야근을 하면 야근 피로도가 쌓임
    # 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더함 : 야근 피로도
    # N 시간 동안 야근 피로도 최소화
    
    # N시간 동안 할 수 있는 모든 경우의 수를 계산
    # 제곱 비교 --> 최솟값 확인
        
    if sum(works) < n:
        return 0

    # 1, 4, 9, 16 , ... : 가장 큰 수부터 빼는 것이 맞음
    # 4 3 3. > 3 3 3 > 2 3 3 > 2 2 3 > 2 2 2
    # 해당 시점에서 가장 큰 수를 1씩 빼는 것으로 진행

    works = Counter(works)
    
    value = max(works.keys())
    
    i = 0
    while i < n: 
        if n - i < works[value]:
            works[value] -= n-i
            works[value-1] += n-i
            i += n-i
            
        else:
            i += works[value]
            works[value-1] += works[value]
            works[value] = 0
            value -= 1
            
    result = [y*(x**2) for x, y in works.items()] 
    return sum(result)


### 최대 힙 방식을 사용한다면, 코드의 효율을 최적화할 수 있다(O(n) -> O(n log k). k는 works 내 고유한 작업량의 개수)

from heapq import heapify, heappop, heappush

def solution(n, works):
    if sum(works) <= n:
        return 0

    # 최대 힙으로 변환 (부호를 반대로 하여 최대값을 최우선으로 뽑기)
    works = [-work for work in works]
    heapify(works)

    for _ in range(n):
        # 가장 큰 작업량을 꺼내서 1 감소
        max_work = heappop(works)
        max_work += 1  # 부호 반대이므로 +1
        heappush(works, max_work)  # 다시 힙에 넣기

    # 결과 계산: 남은 작업량을 제곱한 후 합산
    return sum(work ** 2 for work in works)
