n, k = map(int, input().split())

coin = [int(input()) for _ in range(n)]


dp = [10001]*(k+1)

dp[0] = 0

for i in coin:
    for j in range(i, k+1):
        if dp[j] > 0:
            dp[j] = min(dp[j], dp[j-i] + 1)
        

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
