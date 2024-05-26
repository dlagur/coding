# 가장 무거운 사람, 가장 가벼운 사람을 함께 태우는 것
# 인덱스 : start, end 시점으로 투 포인터 접근
# while : index 같아지는 시점으로 표현

def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    # 필요한 보트의 수 = 보트가 필요한 최대의 경우의 수(모든 인원의 몸무게가 limit인 경우)  - 동시에 들어갈 수 있는 수
    return len(people) - answer
