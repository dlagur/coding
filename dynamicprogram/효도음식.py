# 입력을 받고
n = int(input())
foods = list(map(int, input().split()))

# 좌 -> 우로 훑으며 해당 자리까지 더했을 때의 값 계산하기
minValue = -1001
leftDp = foods[:]
leftDp[0] = foods[0]
for i in range(1, len(foods)):
    leftDp[i] = max(leftDp[i], leftDp[i-1] + leftDp[i])

# 우 -> 좌로 훑으며 해당 자리까지 더했을 때의 값 계산하기
rightDp = foods[:]
rightDp[-1] = foods[-1]
for i in range(len(foods)-2, -1, -1):
    rightDp[i] = max(rightDp[i], rightDp[i+1] + rightDp[i])


# 각 자릿수까지 훑었을 때의 max 값 계산
maxValue = leftDp[0]
for cusor in range(1, len(foods)-1):
    if leftDp[cusor] >= maxValue:
        maxValue = leftDp[cusor]
    leftDp[cusor] = maxValue

maxValue = rightDp[-1]
for cusor in range(len(foods)-2, 0, -1):
    if rightDp[cusor] >= maxValue:
        maxValue = rightDp[cusor]
    rightDp[cusor] = maxValue

# 이후, 붙어있는 재료가 다른 음식을 만드는데 사용되면 안되므로, cursor를 중심으로 +1, -1  씩 연산한 값 계산하기
result = []
for cusor in range(1, len(foods)-1):
    result.append(leftDp[cusor-1] + rightDp[cusor+1])

# 결과적으로, max(result) 출력
print(max(result))
