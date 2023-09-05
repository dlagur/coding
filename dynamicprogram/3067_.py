import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    coins = list(map(int, input().rsplit()))
    want = int(input())

    dp = [0 for _ in range(want+1)]
    dp[0] = 1

    for i in coins:
        for j in range(i, want+1):
            dp[j] += dp[j-i]

    print(dp[want])
