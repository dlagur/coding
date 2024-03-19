n = int(input())
scores = []

for i in range(n):
    student, kor, eng, math = input().split()
    scores.append((student, int(kor), int(eng), int(math)))

# key=lambda x 형식으로 문제에서 주어진 조건 지정 (- : 내림차순, normal : 오름차순)
scores.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in scores:
    print(student[0], end=' ')
