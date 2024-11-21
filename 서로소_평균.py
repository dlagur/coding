# 길이 N인 수열 A에서 X와 서로소인 수를 골라 평균 구함

N = int(input())
numbers = list(map(int, input().split(' ')))
X = int(input())

if X%2 == 0:
    numbers = [num for num in numbers if num%2]
else:
    numbers = [num for num in numbers if num%X != 0]

    
print(int(sum(numbers)/len(numbers)))

#  8 18
# 1 2 4 8
# 1 2 3 6 9 18