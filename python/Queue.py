#!/usr/bin/env python
# coding: utf-8

# In[1]:


# enQueue

queue = [None, None, None, None, None] # 크기가 5인 큐
front = rear = -1 # 초깃값 설정 (비어있는 상태)

rear += 1 # rear = 0
queue[rear] = '화사'

rear += 1 # rear = 1
queue[rear] = '솔라'

rear += 1 # rear =2
queue[rear] = '문별'

print('[출구]<--', end=' ')
for i in range(0, len(queue), 1):
    print(queue[i], end=' ')
print('<--[입구]')


# In[2]:


# deQueue

queue = ['화사', '솔라', '문별', None, None]
front = -1
rear = 2

# 데이터 추출 이전의 큐 상태 확인
print('[출구] <---', end=' ')
for i in range(0, len(queue)):
    print(queue[i], end=' ')
print('<---[입구]')

front += 1
data = queue[front]
queue[front] = None
print('deQueue -->', data)

front += 1
data = queue[front]
queue[front] = None
print('deQueue -->', data)

front += 1
data = queue[front]
queue[front] = None
print('deQueue -->', data)

print('출구 <---', end=' ')
for i in range(0, len(queue), 1):
    print(queue[i], end=' ')
print('<-- 입구')

