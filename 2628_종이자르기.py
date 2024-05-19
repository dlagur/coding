# output : 가장 큰 종이 조각의 넓이
n, m = map(int, input().split())
k = int(input())

cuts = [{0}, {0}]
for i in range(k+1):
    if i == k:
        cuts[0].add(m)
        cuts[1].add(n)
    else:
        d, no = map(int, input().split())
        cuts[d].add(no)

rows, cols = [sorted(cut) for cut in cuts]

max_m, max_n = 0, 0
for i in range(1, len(rows)):
    max_m = max(max_m, rows[i] - rows[i-1])

for i in range(1, len(cols)):
    max_n = max(max_n, cols[i] - cols[i-1])

result = max_m*max_n
print(result)
