n = int(input())
numbers = list(map(int, input().split()))
m = int(input())

indexes = []
for _ in range(m):
    index = list(map(int, input().split()))
    indexes.append(index)

for index in indexes:
    start, end = index
    print(int(numbers[start-1:end] == numbers[::-1][start-1:end]))


import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())

# DP 배열 초기화
dp = [[False] * n for _ in range(n)]

# 길이 1짜리 구간은 항상 팰린드롬
for i in range(n):
    dp[i][i] = True

# 길이 2짜리 구간
for i in range(n - 1):
    if numbers[i] == numbers[i + 1]:
        dp[i][i + 1] = True

# 길이 3 이상 구간
for length in range(3, n + 1):
    for start in range(n - length + 1):
        end = start + length - 1
        if numbers[start] == numbers[end] and dp[start + 1][end - 1]:
            dp[start][end] = True

# 쿼리 처리
for _ in range(m):
    s, e = map(int, input().split())
    print(1 if dp[s - 1][e - 1] else 0)
