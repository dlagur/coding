# <1> r1, c1, r2, c2 범위 안에 있을 때만 배열에 저장하여 메모리 초과 방지
# <2> 같은 길이만큼 2번 진행하고 매 진행마다 방향을 바꿔줌
# <3> 출력 양식을 맞추기 위해 배열에 넣은 값 중 가장 큰 값의 길이만큼 rjust를 사용해 공백처리

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

r1, c1, r2, c2 = map(int, input().split())
hurricane = [[0] for _ in range(c2-c1+1) for _ in range(r2-r1+1)] # 1
total = (c2-c1+1)*(r2-r1+1)
direction = 1

x, y = 0, 0
cnt = 1
l = 1
while total > 0:
    for _ in range(2):
        for _ in range(l):
            if r1 <= x <= r2 and c1 <= y <= c2:
                hurricane[x-r1][y-c1] = cnt
                total -= 1
                m = cnt
            x += dx[direction]
            y += dy[direction]
            cnt += 1
        direction = (direction-1)%4
    l += 1
max_len = len(str(m))
for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        print(str(hurricane[i][j]).rjust(max_len), end="")
    print()
