# output : 가장 긴 조각의 길이 / 그 떄 처음 자르는 위치
## 모든 경우의 수를 고려해야 함
### n-1번 잘랐을 때 가장 긴 조각을 한번 더 자를 수 있으면 n번 자르기, 그렇지 않으면 하지 않기

def dfs(length, row_point, k):
    global max_length
    if k == c:
        print(max_length)
        return
    for p in place:
        max_length = max(length - p, p - row_point)
        dfs(max_length, , k+1)


# main
l, k, c = map(int, input().split())
place = sorted(set(map(int, input().split())))

max_length = 0
dfs(l, 0, 0)
