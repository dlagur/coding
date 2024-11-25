from collections import deque

def solution(begin, target, words):
    # target이 words에 없으면 변환 불가
    if target not in words:
        return 0
    
    # 단어 간 변환 가능 여부를 판단하는 함수
    def can_transform(word1, word2):
        diff_count = sum([word1[i] != word2[i] for i in range(len(word1))])
        return diff_count == 1

    # BFS 탐색
    queue = deque([(begin, 0)])  # (현재 단어, 변환 횟수)
    visited = set()  # 방문한 단어
    
    while queue:
        current_word, step_count = queue.popleft()
        
        if current_word == target:  # 목표 단어에 도달한 경우
            return step_count
        
        for word in words:
            if word not in visited and can_transform(current_word, word):
                visited.add(word)
                queue.append((word, step_count + 1))
    
    return 0  # 변환 불가능한 경우
