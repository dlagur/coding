n, k = map(int, input().split())
dolls = list(map(int, input().split()))

# 슬라이딩 윈도우
left = 0
min_length = float('inf')
lion_count = 0

for right in range(n):
    if dolls[right] == 1:
        lion_count += 1

    # 라이언 인형이 k개 이상일 때 윈도우의 크기 조정
    while lion_count >= k:
        min_length = min(min_length, right - left + 1)
        if dolls[left] == 1:
            lion_count -= 1
        left += 1

# 가능한 경우가 없는 경우 -1 출력
if min_length == float('inf'):
    print(-1)
else:
    print(min_length)




