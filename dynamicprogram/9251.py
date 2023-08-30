import sys
input = sys.stdin.readline

A, B = input().strip(), input().strip()

a, b = len(A), len(B)
cache = [0]*b # cache 생성

for i in range(a):
    cnt = 0
    for j in range(b):
        if cnt < cache[j]:
            cnt = cache[j]
        elif A[i] == B[j]:
            cache[j] = cnt + 1

print(max(cache))
