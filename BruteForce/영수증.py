# 구매한 각 물건의 가격과 개수
# 구매한 물건들의 총 금액

# 총 금액 X
x = int(input())
n = int(input())

# 각 물건의 가격과 개수를 곱한 값(A*B)을 총 금액(X)에서 빼기
for _ in range(n):
    a, b = map(int, input().split())
    x -= a * b

# 총 금액이 0이면 Yes, 아니면 No 출력
if x == 0:
    print("Yes")
else:
    print("No")