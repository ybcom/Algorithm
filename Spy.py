from collections import Counter
from functools import reduce

def solution(clothes):
    answer = 0

    test_dic = Counter([key for value, key in clothes])
    answer = reduce(lambda x, y: x * (y + 1), test_dic.values(), 1) - 1

    return answer