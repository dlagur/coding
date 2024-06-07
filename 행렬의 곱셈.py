def solution(arr1, arr2):
    # 1. 결과값 반환하는 answer 행렬 구조
    answer = [[0 for i in range(len(arr2[0]))] for i in range(len(arr1))]
    # 계산 범위 : 첫번째 행렬 각 행 , 두번째 행렬 각 행의 동일 index

    # 계산
    for row in range(len(answer)):
        for col in range(len(answer[0])):
            for i in range(len(arr2)):
                answer[row][col] += arr1[row][i]*arr2[i][col]

    return answer


# 다른 사람의 풀이
def productMatrix(X, Y):
    answer = [[sum(a*b for a, b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

    return answer
