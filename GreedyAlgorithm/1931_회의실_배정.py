#!/usr/bin/env python
# coding: utf-8

# In[1]:


N = int(input())
conference = []
alignment = []

# conference 리스트 만들기
for i in range(N):
    start, end = input().split()
    start = int(start); end = int(end)
    conference.append((start, end))
    if start > end:
        conference.remove(conference[-1])

conference.sort(key=lambda x:(x[1], x[0])) # key에 튜플로 여러 인자들을 주면 해당 인자의 순서대로 정렬을 해준다

alignment.append(conference[0])
conference.remove(conference[0])

while len(conference) != 0:
    if alignment[-1][1] > conference[0][0]:
        conference.remove(conference[0])
    else:
        alignment.append(conference[0])
        conference.remove(conference[0])
        # 제약 조건을 걸어놔야함 -> 최대 사용할 수 있는 회의실의 개수(N)

print(len(alignment))


# In[26]:


11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 1


# In[6]:


N = int(input())
time = sorted([tuple(map(int, input().split())) for i in range(N)], key=lambda x:(x[1], x[0]))
ans = end = 0
for s,e in time:
    if s >= end:
        ans += 1
        end = e
print(ans)

