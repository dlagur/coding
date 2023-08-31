n = int(input())

d = [0]*100001

d[1] = 3
d[2] = 7


for i in range(3, n+1):
    d[i] = (d[i-2] + d[i-1]*2)%9901

print(d[n])
