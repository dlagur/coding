n = int(input())

places = list(map(int, input().split()))
places.sort() # 오름차순 정렬

result = 100000

for place in places:
    expect = list(map(lambda x: x-place, places))
    distance = sum(expect)

    if distance < result:
        result = distance
        l = place

print(l) # 합이 최소가 되는 지점
