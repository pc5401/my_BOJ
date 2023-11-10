import sys
import itertools
import collections
input = sys.stdin.readline

def stack_sum(num: int, table: list)->list:
    rtn = collections.defaultdict(int)
    c = itertools.cycle(table)
    
    for i in range(num):
        v = 0
        for j in range(num-1):
            v += next(c)
            if rtn[v]:
                rtn[v] += 1
            else:
                rtn[v] = 1
    
    rtn[0] = 1
    rtn[sum(table)] = 1

    return rtn


if __name__ == "__main__":
    S = int(input()) # size
    M, N = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    B = [int(input()) for _ in range(N)]

    # 만들 수 있는 조합의 값 계산
    val_A = stack_sum(M, A)
    val_B = stack_sum(N, B)
    res = 0
    for key in val_A:
        diff = S - key
        if val_B[diff]:
            res += (val_A[key]*val_B[diff])

    print(res)

