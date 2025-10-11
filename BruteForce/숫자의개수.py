a = int(input())
b = int(input())
c = int(input())

# A*B*C 세 수의 곱 저장
abc = a*b*c

# 0~9까지의 개수를 저장할 리스트
num = [0]*10

# 문자열로 변환 후 각 자리수의 개수를 세기
for i in str(abc):
    num[int(i)] += 1

# 각 자리수의 개수 출력
for j in num:
    print(j) 