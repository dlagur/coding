import sys
input = sys.stdin.readline

n = int(input())
grape = [int(input()) for _ in range(n)]

d = [0]*10000
d[0] = grape[0]
d[1] = grape[0] + grape[1]
d[2] = max(grape[2] + grape[0], grape[2] + grape[1], d[1])

for i in range(3, n):
    d[i] = max(grape[i] + d[i-2], grape[i] + grape[i-1] + d[i-3], d[i-1])

print(max(d))
