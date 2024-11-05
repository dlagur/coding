def solution(triangle):
    # dp 배열을 triangle 배열과 동일한 크기로 초기화
    dp = [row[:] for row in triangle]

    # 두 번째 줄부터 각 위치에서 최대 합을 계산
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0: # 맨 왼쪽은 위의 바로 위 칸만 더함
                dp[i][j] += dp[i-1][j]
            elif j == len(triangle[i]) - 1: # 맨 오른쪽은 위의 바로 왼쪽만 더함
                dp[i][j] += dp[i-1][j-1]
            else: # 중간은 왼쪽 위와 위 중 큰 값을 더함
                dp[i][j] += max(dp[i-1][j-1], dp[i-1], [j])
    return max(dp[-1])

# solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])
