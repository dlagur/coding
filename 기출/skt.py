"""
제한 사항: 10초, 2GB
### 문제 정의:

전시회가 매일 열리고, 사람들은 전시를 관람하며 지인들에게 전시를 추천합니다. 지인 관계는 리스트로 주어지며, 추천 받은 사람만 전시를 관람할 수 있습니다.
같은 테마의 전시는 한 사람이 최대 두 번까지만 관람할 수 있습니다. 새로운 테마의 전시가 시작되면 다시 관람할 수 있지만, 여전히 추천을 받아야 합니다.

**입력:**

1. `exhibitions`: 전시 테마 목록 (리스트 형태, 길이 N)
2. `connections`: 지인 연결 관계를 나타내는 리스트 (각 요소는 `[a, b]` 형태로 a와 b가 지인임을 나타냄)

**출력:** 매일 몇 명이 전시를 관람하는지를 나타내는 리스트

### 조건:

- 1번 사람은 처음 날에만 자발적으로 전시를 관람하고, 이후로는 추천을 받아야만 관람할 수 있습니다.
- 한 사람이 같은 전시 테마를 최대 두 번까지만 관람할 수 있습니다.
- 새로운 전시가 시작되면 다시 관람할 수 있지만, 여전히 추천을 받아야 합니다.
- 같은 테마의 전시를 두 번 관람한 사람은 그 테마를 더 이상 관람하거나 추천하지 않습니다.
"""

def sol(exhibitions: list, connections: list) -> list:

# Test Case
connections = [[1,2], [1,4], [3,4], [4,5], [5,6], [6,7], [7,8]]
#5일간 열리는 전시회 목록
exhibitions = ['pop', 'pop', 'pop', 'landscape', 'landscape']

# 과정 :
## 1일차 : 1 관람 -> 2, 4 추천
## 2일차 : 2, 4 관람 -> 1, 3, 5 추천
## 3일차 : 1,3,5 관람 -> 2,4,5, 6 추천
###### 전시 바뀜
## 4일차 : 2,4,5,6 관람 -> 1,3,4,6,7 추천
# 5일차 : 1,3,4,6,7

# output = [1,2,3,4,5]

# 전시회 방문횟수 체크
bp = [0]*(connections[-1][-1] + 1) #

result = []
def bfs():
    q = [1]
    i = 0
    Flag = exhibitions[0] # 전시회 주제 변경 여부

    while i < len(exhibitions):
        if Flag != exhibitions[i]:
            Flag = exhibitions[i]
            bp = [0] * (connections[-1][-1] + 1)
        result.append(len(q))
        for n in q:
            if bp[n] < 2:
                bp[n] += 1
                conn = {num[1] for num in connections if n in num and bp[n] < 2} # {2, 4}
        conn = list(conn)
        i += 1

bfs()


## connection 리스트를 인접 행렬, 인접 리스트로 표현하기

# 인접 리스트 생성
adj_list = {}
for u, v in connections:
    if u not in adj_list:
        adj_list[u] = []
    if v not in adj_list:
        adj_list[v] = []
    adj_list[u].append(v)
    adj_list[v].append(u)

def bfs():
    q = [1]
    i = 0
    Flag = exhibitions[0]  # 전시회 주제 변경 여부
    bp = [0] * (max(adj_list) + 1)

    while i < len(exhibitions):
        if Flag != exhibitions[i]:
            Flag = exhibitions[i]
            bp = [0] * (max(adj_list) + 1)

        result.append(len(q))
        next_q = []

        for n in q:
            if bp[n] < 2:
                bp[n] += 1
                for neighbor in adj_list.get(n, []):  # 인접 리스트를 사용
                    if bp[neighbor] < 2:
                        next_q.append(neighbor)

        q = next_q
        i += 1

bfs()

### 시간 복잡도 O(N*M) --> O(N+M)으로 효율성 증대
### 공간 복잡도 : O(connection 내 원소의 개수) : 알아서 제한 뒀을 듯
