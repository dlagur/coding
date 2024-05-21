def solution(N):

    binary = format(N, 'b')

    gap, count = 0, 0

    for i in binary:
        if '1' == i:
            if count > gap:
                gap = count
            count = 0
        else:
            count += 1

    return gap
