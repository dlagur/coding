string = input()

stack = []
depth_result = [0] * 50 # depth check 용도
depth = 0

for ch in string:
    if ch != ")":
        if ch == "(":
            depth += 1 # 괄호 차수 확인
            depth_result[depth] = 0
        stack += [ch]
    else:
        #  ')' 시 계산
        for i in range(len(stack) - 1, -1, -1): # 역순 탐색
            if stack[i] == "(":
                num = depth_result[depth]
                for j in stack[i + 1 :]: # 괄호 안에 있는 문자열 길이 세기
                    num += 1
                depth -= 1
                depth_result[depth] += num * int(stack[i - 1]) # 문자열 길이 계산 및 차수에 추가
                del stack[i - 1 :] # 계산한 값 제거

                break
print(depth_result[0] + len(stack))

#### 수정한 코드
string = input()

stack = []
depth_result = [0] * 50 # depth check 용도
depth = 0

for ch in string:
    if ch != ")":
        if ch == "(":
            depth += 1 # 괄호 차수 확인
            depth_result[depth] = 0
        stack += [ch]
    else:
        #  ')' 시 계산
        for i in range(len(stack) - 1, -1, -1): # 역순 탐색
            if stack[i] == "(":
                num = depth_result[depth]
                num += len(stack[i+1:]) # 괄호 안에 있는 문자열 길이 세기 # 에러 나지 않음
                depth -= 1 # 괄호 차수 감소
                depth_result[depth] += num * int(stack[i - 1]) # 문자열 길이*괄호 바로 앞 숫자 곱하여 더하기
                del stack[i - 1 :] # 계산한 값 제거(괄호 앞 숫자부터 stack의 끝까지)
                break # else 내 for 문 종료
print(depth_result[0] + len(stack))
