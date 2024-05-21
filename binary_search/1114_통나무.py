from sys import stdin

input = stdin.readline

def main():
    L, K, C = map(int, input().split())
    positions = [0, *sorted([*map(int, input().split())]), L]
    # * : python에서 unpacking 연산자로 사용되며, 이터러블의 요소들을 개별 요소로 풀어내는 역할을 한다
    # 리스트를 이어붙이고 싶을 때 사용하면 된다
    pieces = [positions[idx+1] - positions[idx] for idx in range(K+1)]
    # 자를 수 있는 모든 포인트 간 거리 구하기 --> pieces
    longest = max(pieces)
    # 가장 긴 것 --> longest에 저장

    def solve(mid): # mid : 기준
        if longest > mid:   # 현재 기준으로 자를 수 없는 나무 조각이 있는 경우.
            return 10001, 0
        sums_ = 0
        count = 0
        for piece in pieces[::-1]:
            sums_ += piece      # 나무조각 길이를 누적 합
            if sums_ > mid:     # 기준이 넘어가면
                sums_ = piece   # 새로운 조각으로 취급
                count += 1
        return count, sums_ if count == C else pieces[0]

    left = 0
    right = L
    while left <= right:
        mid = (left + right) // 2   # 나무조각 하나의 최대 길이

        count, front = solve(mid)
        if count <= C:              # 조각을 더 작게 자를 수 있는 방향으로 update
            ans_longest = mid
            ans_front = front
            right = mid - 1
        else:                       # 조각을 더 크게 자를 수 있는 방향으로 update
            left = mid + 1

    print(ans_longest, ans_front)

if __name__ == "__main__":
    main()
