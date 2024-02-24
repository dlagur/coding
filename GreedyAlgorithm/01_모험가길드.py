n = int(input())
horror = map(int, input().split())

horror.sort() # O(nlogn) : 오름차순 정렬
count, result = 0, 0

for h in horror:
    count += 1
    if count >= h:
        # 최대의 그룹 수를 만드는 것이 목표이므로, count에 더한 후 그 값이 h가 넘어가면 count 초기화
        result += 1
        count = 0

print(result)
