n = int(input())

fibo = [0,1] + [0]*(n-1)

for i in range(2, len(fibo)):
    fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo[17])
