def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    ## 1000 이하의 자연수이므로, 3자리간 비교
    # 문자열 간 대소비교는 자릿수만 비교 한다 Ex. '765' > '742999' 가 가능하다
    return str(int(''.join(numbers)))
