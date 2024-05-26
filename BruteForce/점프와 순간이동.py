# k칸 앞으로 점프 / 현재까지 온 거리*2
# 건전지 => k칸 점프 시 k만큼의 건전지 사용량 증가
def solution(n):
    result = 0

    while n > 0:
        n, ans = n // 2, n % 2
        result += ans

    return result
