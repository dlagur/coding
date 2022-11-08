#!/usr/bin/env python
# coding: utf-8

# In[58]:


N, k = map(int, input().split())
A = []
sum_coin = 0

for i in range(N):
    A.append(int(input()))   
A.sort(reverse=True)

for i in A: 
    sum_coin += k//i
    k = k%i
    
print(sum_coin)

