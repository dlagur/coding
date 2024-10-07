'''
백준 11723번

시간 제한 : 1.5초
메모리 제한 : 4MB
'''


# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.

import sys
input = sys.stdin.readline
m = int(input())
s = 0b0 # 이진수 표현

# 000 000 000 000 000 000 00 / 0
# 0 -> 집합에 해당 원소 x
# 1 -> 집합에 해당 원소 o

for _ in range(m):
    command = input()
    # add 3 / all, empty
    try:
        com, n = command.split()
        n = int(n)
        if com == 'add': # 없으면 n을 추가(0|1 = 1), 있으면 커맨드 무시(1|1 = 1)
            s = s | (0b1 << n)
            # 5자리, s = {3}
            # add 3
            # 00100 | 00100  = 00100
        elif com == 'remove': # 있으면 n을 제거(1 & 0 =  0), 없으면 커맨드 무시(0 & 0  = 0)
            s = s & ~(0b1 << n)
            # remove 3
            # 00100 & ~00100(=11011) --> 00000 s = {}
        elif com == 'check': # 위치에 있으면 1, 없으면 0
            if (s & (0b1 << n)):
                # check 3
                # 00100 & 00100  = 00100
                print(1)
            else:
                # check 2
                print(0)
        elif com == 'toggle': # 있으면 제거(1 ^ 1 = 0), 없으면 추가(1 ^ 0 = 1)
            s = s ^ (0b1 << n) # ^ XOR

    except: # try 첫 행에서 에러 발생
        if command == 'all':
            s = 0b11111111111111111111
        elif command == 'empty':
            s = 0b0

