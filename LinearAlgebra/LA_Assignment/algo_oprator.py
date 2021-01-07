'''
풀이법
아오 뭐야 그냥 내가 메모리 별로일거 같다는 방법이 맞아쓰..

나눗셈의 계산처리 문제
어떻게 음수 나눗셈과 양수 나눗셈 계산을 할건가.
int(x/y) 로 해결
'''
import itertools
from functools import reduce

if __name__ == "__main__":
    num = int(input())
    num_value = [int(a) for a in input().split(' ')]
    num_operator = [int(a) for a in input().split(' ')]

    operator_list = []
    list(operator_list.extend([str(i)] * v) for i, v in enumerate(num_operator)
         if v > 0)
    operator_permutation = [list(a) for a in
                            set(itertools.permutations(operator_list))]

    operator = {
        '0': lambda x, y: x + y,
        '1': lambda x, y: x - y,
        '2': lambda x, y: x * y,
        '3': lambda x, y: int(x/y)
    }

    value = []
    for cur_permu in operator_permutation:
        value.append(
            reduce(lambda x, y: operator[cur_permu.pop()](x, y), num_value))
    print(max(value), min(value))
