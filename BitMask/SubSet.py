def subset_sum(arr, target):
    n = len(arr)

    # 모든 가능한 부분 집합을 탐색
    for mask in range(1 << n):  # 1 << n은 2^n을 의미하며, 모든 부분 집합을 나타냄
        subset_sum = 0

        # 각 숫자가 부분 집합에 포함되는지 확인
        for i in range(n):
            if mask & (1 << i):  # i번째 숫자가 부분 집합에 포함된다면
                subset_sum += arr[i]

        # 부분 집합의 합이 target과 같다면 "YES"를 반환
        if subset_sum == target:
            return "YES"

    # 모든 부분 집합을 확인했지만 target과 같은 합이 없는 경우 "NO"를 반환
    return "NO"


# 입력 예시
n = int(input("배열의 크기 n을 입력하세요: "))
arr = list(map(int, input("배열의 요소를 입력하세요: ").split()))
target = int(input("목표 정수 target을 입력하세요: "))

# 결과 출력
print(subset_sum(arr, target))
