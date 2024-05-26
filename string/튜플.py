def solution(s):
    result = []

    # 대괄호 제거하기
    s = s[2:-2]
    s = s.split('},{')

    for i in range(len(s)):
        s[i] = s[i].split(',')

    s.sort(key=lambda x: len(x))

    for str in s:
        for i in str:
            if int(i) not in result:
                result.append(int(i))

    return tuple(result)



# 다른 사람의 풀이
import re
from collections import Counter

def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))
