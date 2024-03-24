n, x = map(int, input().split())

array = list(map(int, input().split()))

result = 0
def binary_search(array, target, start, end):
    global result
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        result += 1
        return binary_search(array, target, start, mid - 1)
        return binary_search(array, target, mid + 1, end)
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

binary_search(array, 2, 0, n-1)

if result > 0:
    print(result)
else:
    print(-1)
