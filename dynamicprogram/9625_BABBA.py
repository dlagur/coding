k = int(input())

fibo = [0]*46

fibo[1] = 1
fibo[2] = 1

for i in range(3, 46):
    fibo[i] = fibo[i-1] + fibo[i-2]

print(A[k-1], B[k], end=' ')
