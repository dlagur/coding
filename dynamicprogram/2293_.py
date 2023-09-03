n, k = map(int, input().split())

coin = [int(input()) for _ in range(n)]

d = [0]*10001 # d[i] :  i원이 될 수 있는 경우의 수

d[0] = 1 # 동전을 1개만 쓸 때의 경우의 수

for i in coin:
    for j in range(i, k+1):
        if j-i >= 0:
            d[j] += d[j-i]

print(d[k])
