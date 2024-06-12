def solution(progresses, speeds):
    answer = []

    # 100 이상이 되게끔 하는 일 수를 찾고
    for i in range(len(speeds)):
        if (100 - progresses[i]) % speeds[i]:
            progresses[i] = (100 - progresses[i]) // speeds[i] + 1
        else:
            progresses[i] = (100 - progresses[i]) // speeds[i]

    # 앞 원소가 100이 되는 시점과 비교
    # 앞 원소의 시점이 현재 원소의 시점보다 늦으면 배포에 포함
    start = progresses[0]
    deploy = 1
    for i in range(1, len(progresses)):
        if start >= progresses[i]:
            deploy += 1
        else:
            answer.append(deploy)
            start = progresses[i]
            deploy = 1

    answer.append(deploy)
    return answer
