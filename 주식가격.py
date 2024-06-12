def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        if stack != []:
            while stack != [] and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer

def solution(prices):
    answer = [0]*len(prices)

    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                if i != len(prices) - 1:
                    answer[i] += 1
                break
    return answer
