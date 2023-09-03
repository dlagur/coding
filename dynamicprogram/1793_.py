dp = [0]*251

# 입력 개수에 제한 받지 않고 받기
while True:
    try: # 입력받을 값이 있다면 진행
        n = int(input())
        dp[0] = 1
        dp[1] = 1
        dp[2] = 3

        for i in range(3, 251):
            dp[i] = 2*dp[i-2] + dp[i-1] # 점화식
        print(dp[n])
    except: # 없으면 종료
        break
