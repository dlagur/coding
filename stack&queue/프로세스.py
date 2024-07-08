# Q에서 대기중인 프로세스 하나를 꺼낸다
# Q에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 Q에 넣는다
# 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스 실행
from collections import deque

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    queue = deque(queue)
    answer = 0
    while True:
        cur = queue.popleft()
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
