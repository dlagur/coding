def solution(k, tangerine):
    answer = 0
    # 딕셔너리 생성
    g = {}
    # 귤 갯수 확인
    for t in tangerine:
        g[t] = g.get(t, 0) + 1

    g = sorted(g.values(), reverse=True)  # O(nlogn)
    # 그리디 방식으로 k를 만족시키는 최소 귤 종류 선정
    # 가장 많은 개수를 가진 귤의 갯수부터 정리

    n = 0
    for i in g:
        answer += 1
        n += i
        if n >= k:
            break

    return answer
