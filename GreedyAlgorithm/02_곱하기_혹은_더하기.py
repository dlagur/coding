S = list(input()) # 입력 값 리스트로 받기

nums = [int(i) for i in S]
result = 0

for num in nums:
    # num이나 result 값이 0, 1의 값을 가질 때, 덧셈 진행
    if num in [0, 1] or result in[0, 1]:
        result += num
    else:
        result *= num

print(num)
