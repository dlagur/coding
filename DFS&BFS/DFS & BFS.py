#!/usr/bin/env python
# coding: utf-8

# In[1]:


stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)


# In[2]:


print(stack[::-1]) # 최하단부터 출력


# In[4]:


from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()

queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)


# In[ ]:


def recursive_function():
    print('재귀 함수를 호출합니다')
    recursive_function()
    
recursive_function()


# In[3]:


def recursive_function(i):
    
    if i == 100 :
        return
    print(i, '번째 재귀 함수에서', i+1, '번째 재귀함수를 호출합니다')
    recursive_function(i+1)
    print(i, '번째 재귀함수를 종료합니다')

recursive_function(1)


# In[4]:


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    
    return result

def recursive(n):
    if n <= 1:
        return 1
    
    return n * recursive(n-1)

print(factorial(5))
print(recursive(5))


# In[5]:


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)
    
print(gcd(192, 162))


# In[6]:


# 재귀함수를 잘 사용하면 복잡한 알고리즘을 간결하게 작성할 수 있다
# 단, 다른 사람이 이해하기 어려운 형태의 코드가 될 수 있으므로 신중히 사용해야 한다.
# 모든 재귀함수는 반복문을 이용하여 동일한 기능을 구현할 수 있습니다.
# 반복문보다 유리할수도, 불리할수도 있다.


# In[8]:


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
# 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
    [],
    [2,3,8], # 1번 노드와 연결
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 표현
visited = [False] * 9 
    
dfs(graph, 1, visited)


# In[10]:


from collections import deque

def bfs(graph, start, visited):
    # queue 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
    [],
    [2,3,8], # 1번 노드와 연결
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
bfs(graph, 1, visited)

