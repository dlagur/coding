import sys
input = sys.stdin.readline

n = int(input())

stairs = [0]
d = [0]*(n+1)

for i in range(1, n+1):
    x = int(input())
    stairs.append(x)

if n <= 2:
    print(sum(stairs))

else:
    d[1] = stairs[1]
    d[2] = stairs[1] + stairs[2]
    for i in range(2, n+1):
        d[i] = max(d[i-2] + stairs[i], d[i-3] + stairs[i-1] + stairs[i])
    print(d[n])
