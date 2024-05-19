# 100 * 100 매트릭스 생성
matrix = [[0]*100 for _ in range(100+1)]

cnt = 0

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    #점 좌표가 아닌 박스 좌표로 변환
    for i in range(x1, x2):
        for j in range(y1, y2):
            if not matrix[i][j]:
                matrix[i][j] = 1
                cnt += 1

print(cnt)
