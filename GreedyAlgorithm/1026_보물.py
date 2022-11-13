#!/usr/bin/env python
# coding: utf-8

# In[25]:


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(); temp_B = B.copy();
sorted_A = [0 for i in range(N)]

for i in range(N):
    sorted_A[temp_B.index(max(temp_B))] = A[i]
    temp_B[temp_B.index(max(temp_B))] = -1
    
A = sorted_A

s = 0
for j in range(N):
    s += A[j]*B[j]    
    
print(s)

