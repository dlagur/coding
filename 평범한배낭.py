import sys
input = sys.stdin.readline

N, K = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(K+1) for _ in range(N+1)]
# DP표는 0~K+1, 0~N+1로 구성
# (N=1일 때, DP[i-1][j]가 존재해야 하므로)

for i in range(1,N+1):
    for j in range(1,K+1):
        if j >= bag[i-1][0]:  # 현재 최대 무게 j가 해당 물건 무게보다 큰 경우
        #표의 윗 셀의 값과 (현재 물건의 V + 이전 물건의 V 값) 중의 최댓값을 DP[i][j]에 저장
            dp[i][j] = max(bag[i-1][1]+dp[i-1][j-bag[i-1][0]],dp[i-1][j])
            # bag[i-1][1] : 현재 물건의 V
            # j - bag[i-1][0] : j에서 무게를 뺀값 ex) v(14) = v(6) + v(8)
            ## 만약 현재 물건의 v가 k와 같다면 이전 물건의 v 값은 당연히 0이다.
        else:
        	# 현재 최대무게 j가 해당 물건무게보다 작은 경우 (현재 물건을 담을 수 없는 경우)
            dp[i][j] = dp[i-1][j]

print(dp[N][K])  #DP[N][K]가 무조건 정답
