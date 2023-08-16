n = int(input())

cases = [0]*1000001

cases[1] = 1
cases[2] = 2

for i in range(3,len(cases)):
    cases[i] = (cases[i-1] + cases[i-2])%15746

print(cases[n])
