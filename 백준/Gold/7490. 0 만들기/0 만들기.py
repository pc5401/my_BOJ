import sys
import functools
import itertools
input = sys.stdin.readline

def calculate(n: int, cobi: list, possible_zero_formula:list):
    formula = '1'
    for i in range(2, n+1):
        if cobi[i - 2] == 0:
            formula += f'{i}'
        elif cobi[i - 2] == 1:
            formula += f'+{i}'
        elif cobi[i - 2] == 2:
            formula += f'-{i}'

    if eval(formula) == 0:
        formula = '1'
        for i in range(2, n+1):
            if cobi[i - 2] == 0:
                formula += f' {i}'
            elif cobi[i - 2] == 1:
                formula += f'+{i}'
            elif cobi[i - 2] == 2:
                formula += f'-{i}'
        possible_zero_formula.append(formula)


@functools.cache
def main(n: int):
    possible_zero_formula = []
    
    for cobi in itertools.product(range(3), repeat=n-1):
        calculate(n, cobi, possible_zero_formula)
    
    possible_zero_formula.sort()
    rtn = ''
    
    for zero_formula in possible_zero_formula:
        rtn += (zero_formula+'\n')

    return rtn


if __name__ == '__main__':
    # 입력값
    T = int(input())
    res = []
    for tc in range(T):
        N = int(input())
        res.append(main(N))

    for r in res:
        print(r)