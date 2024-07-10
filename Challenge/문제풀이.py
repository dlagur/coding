
# 시간 복잡도 : O(n*n!)
# n = 9 이상부터 처리하기 어려움
from itertools import permutations

n_list = list(input())

result = []
s = int(''.join(n_list))

for l in permutations(n_list):
    a = int(''.join(l))
    if s < a:
        result.append(a)

result.sort()
print(result[0])


### 다른 풀이
# 시간 복잡도 : O(n)
# 10^6의 input이 들어왔을 때도 처리 가능
s = list(input())
# 역순으로 탐색하여 감소하는 지점 찾기
# 문자열의 끝에서 시작하여 처음으로 감소하는 지점 찾기
## 주어진 숫자보다 큰 다음 숫자를 찾기 위해 필요한 단계
for i in range(len(s) - 2, -1, -1):
    if s[i] < s[i + 1]:
        break
else:
    ## 만약 비내림차순이라면, 0을 출력하고 종료
    print(0)
    exit() # 스크립트 실행 종료


# 교환할 지점 찾기
## 문자열의 끝에서부터 다시 시작하여 s[i]보다 큰 첫번째 요소를 찾고, 두 요소를 교환
for j in range(len(s) - 1, i, -1):
    if s[j] > s[i]:
        break
s[i], s[j] = s[j], s[i]
# 두 요소 교환

# 뒤쪽 부분 뒤집기
## S[i] 이후의 모든 요소를 역순으로 정렬 : 사전식으로 가장 작은 순열을 만들기 위함
s[i+1:] = s[:i:-1]
print("".join(s))
