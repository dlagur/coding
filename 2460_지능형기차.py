# 10개의 정착역
# output : 출발역에서 종착역까지 가는 도중 기차 안에 사람이 가장 많을 때의 사람 수

count = 0
for _ in range(10):
    a, b = map(int, input().split())
    result = max(result, count + (b-a))
    count += (b - a)

print(result)
