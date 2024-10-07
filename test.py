def recursion(arr, N):

    top_left = [i[:(N//2)] for i in arr[:(N//2)]] # 가로로 분할
    top_right = [i[(N//2):] for i in arr[:(N//2)]]
    bottom_left = [i[:(N//2)] for i in arr[(N//2):]]
    bottom_right = [i[(N//2):] for i in arr[(N//2):]]

    # 재귀
    temp = [recursion(top_left, N//2), recursion(top_right, N//2),
            recursion(bottom_left, N//2), recursion(bottom_right, N//2)]

    temp.sort()
    return temp[1]

print(recursion(arr, N))
