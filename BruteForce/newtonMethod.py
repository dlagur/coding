x = int(input())

def newton_method(x):
    if x == 0:
        return 0
    estimate = x / 2.0 # 초기 추정값 설정
    tolerance = 1e-7 # 허용 오차 설정
    max_iterations = 1000 # 최대 반복 횟수 설정
    for _ in range(max_iterations):
        next_estimate = (estimate + x / estimate) / 2.0
        if abs(next_estimate - estimate) < tolerance:
            return next_estimate
        estimate = next_estimate
    return estimate