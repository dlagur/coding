import sys
input = sys.stdin.readline

# 자두가 떨어지는 시간 t와 이동할 수 있는 횟수 w
t, w = map(int, input().split())

# 자두가 떨어지는 나무의 번호 저장
tree = [0]
for i in range(t):
    tree.append(int(input()))

# 2차원 dp 테이블 초기화 
dp = [[0]*(w+1) for _ in range(t+1)] # dp 테이블 생성

for i in range(t+1):

    # 1번 나무에서 한 번도 움직이지 않는 경우

    # 1번 나무에서 자두가 떨어진다면
    if tree[i] == 1:
        dp[i][0] = dp[i-1][0] + 1
    
    # 2번 나무에서 자두가 떨어진다면
    else:
        dp[i][0] = dp[i-1][0]

    # 1번 이상 움직이는 경우에 대해 탐색
    for j in range(1, w+1):

        # i초에 2번 나무에서 자두가 떨어지고, 현재 2번 나무에 위치
        if tree[i] == 2 and j%2 == 1:
            # 이전 위치에서 움직여 받아 먹을 것인지, 현재 위치에서 받아 먹을 것인지 결정
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        
        # i초에 1번 나무에서 자두가 떨어지고, 현재 1번 나무에 위치
        elif tree[i] == 1 and j%2 == 0:
            # 이전 위치에서 움직여 받아 먹을 것인지, 현재 위치에서 받아 먹을 것인지 결정
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1

        # i초에 자두가 떨어지는 나무와 현재 나무의 위치가 다른 경우
        else:
            # 움직여 못 먹는 경우와 움직이지 않아서 못 먹는 경우 비교
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])
        
# DP 테이블의 마지막 행의 최댓값 출력
print(max(dp[t]))
