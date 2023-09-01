import sys
input = sys.stdin.readline

N, D = map(int, input().split())

dist = [list(map(int, input().split())) for _ in range(N)]

d = [i for i in range(D+1)]

for i in range(D+1):
    if i > 0:
        d[i] = min(d[i], d[i-1]+1)
    for s, e, short in dist:
        if i == s and e <= D and d[i]+ short < d[e]:
            d[e] = d[i] + short

print(d[D]) 
