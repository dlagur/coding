def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)

    low = 1
    high = distance

    answer = 0

    while low <= high:
        mid = (low + high) // 2

        left_rock = 0
        count = 0
        for i in range(len(rocks)):
            right_rock = rocks[i]

            if right_rock - left_rock < mid:
                count += 1

            else:
                left_rock = right_rock

        if count <= n:
            answer = mid
            low = mid + 1

        else:
            high = mid - 1

    return answer
