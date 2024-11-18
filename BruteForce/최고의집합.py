def solution(n, s):
    if n > s:
        return [-1]
    
    if s%n == 0:
        return [s//n for _ in range(n)]
    
    else:
        answer = [s//n for _ in range(n - s%n)] + [s//n + 1 for _ in range(s%n)]
        return answer
