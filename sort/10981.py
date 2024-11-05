n, k = map(int, input().split())
info = {}

for _ in range(n):
    univ, name, pros, pen = input().split()
    pros = int(pros)
    pen = int(pen)

    temp = info.get(univ, [None, 0, float('inf')])

    # 대학별 최고 문제 해결 수가 많은 팀 혹은 동일한 해결 수 중 패널티가 적은 팀 선택
    if temp[1] < pros or (temp[1] == pros and temp[2] > pen):
        info[univ] = [name, pros, pen]

# 문제 해결 수는 내림차순, 패널티는 오름차순으로 정렬
result = sorted(info.values(), key=lambda x: (-x[1], x[2]))

# 상위 k개의 팀 출력
for i in range(k):
    print(result[i][0])
