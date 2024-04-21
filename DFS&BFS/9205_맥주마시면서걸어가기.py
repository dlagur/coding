# 집 -> 축제에 가는 문제
# 50m당 1병씩. 맥주를 마셔야 함
# 맥주를 최대한 가져올 수 있는 개수는 20병.
# 집과 축제 장소 간 편의점이 위치.

# 출력값은 --> 가지고 있는 맥주 수 안에서 축제 장소에 온전히 갈 수 있는가(맥주를 끊기지 않고 마시고 갈 수 있는가)
# 있으면 happy | 없으면 bad
# 편의점은 갈 수도 있고, 가지 않을 수도 있다.

# 갈 수 있냐는 의미 == 주어진 조건 하에서 갈 수 있느냐? ==> 갈 수 있는 경우의 수를 구하는 것이 아니라, 갈 수 있느냐만 따지면 되는 것.
# BFS로 접근

from collections import deque

# bfs
def bfs():
   q = deque()
   q.append((start_x, start_y))
   # 맨해튼 거리 == x의 차 + y의 차
   while q:
       x, y = q.popleft()
       if abs(end_x - x) + abs(end_y - y) <= 1000:
           print('happy')
           return
       # 편의점을 거치는 경우의 수를 계산하는 부분
       for i in range(n):
           if not visited[i]:
               # 우선, 현 위치에서 편의점에 갈 수 있는지를 판단
                nx, ny = graph[i]
                if abs(nx-x) + abs(ny-y) <= 1000:
                    visited[i] = 1
                    q.append((nx, ny))
   # 이렇게 while문을 지정하게 되면, 현 위치로부터 1000m이내에 위치한 편의점들을 모두 방문처리를 하면서,
   # 각각 그 위치의 편의점을 방문했을 때의 이후 경로를 모두 찾아볼 수 있는 코드가 됩니다.
   print('sad')
   return

# main
t = int(input())

for _ in range(t):
    n = int(input())
    graph = []

    # 집 위치
    start_x, start_y = map(int, input().split())
    # 편의점 위치
    for _ in range(n):
        x, y = map(int, input().split())
        graph.append((x, y))
    # 목적지 위치
    end_x, end_y = map(int, input().split())
    visited = [0 for _ in range(len(graph))]
    bfs()




