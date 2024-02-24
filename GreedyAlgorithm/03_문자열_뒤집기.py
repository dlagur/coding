S = list(input())

count = 0
standard = S[0]


for num in S[1:]:
    if num == standard:
        pass
    else:
        count += 1
        standard = num

# 바뀌는 지점은, count = 2로 카운트된다.
if count%2 == 0:
    print(count//2)
else:
    print(count//2 + 1)
