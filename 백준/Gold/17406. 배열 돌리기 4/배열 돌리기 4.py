import sys
import copy
import itertools
input = sys.stdin.readline


def turn_arr(r: list, c: int, S: int, A: list):

    for s in range(S,0,-1):
        start_v = A[r-s][c-s]
        for i in range(r-s, r+s): # 왼쪽측
            A[i][c-s] = A[i+1][c-s]
        i += 1
        for j in range(c-s, c+s): # 아래쪽
            A[i][j] = A[i][j+1]
        j += 1

        while r-s < i:
            A[i][j] = A[i-1][j]
            i -= 1

        while c-s < j:
            A[i][j] = A[i][j-1]
            j -= 1
        
        A[i][j+1] = start_v


def solve(turn_lst: list):
    A = copy.deepcopy(Arr)

    for R,C,S in turn_lst:
        turn_arr(R-1, C-1, S, A)
    
    rtn = float('INF')

    for a in A:
        rtn = min(rtn, sum(a))
    return rtn


if __name__ == '__main__':
    N, M, K = map(int,input().split())
    Arr = [list(map(int, input().split())) for _ in range(N)]
    lst = [list(map(int,input().split())) for _ in range(K)]
    res = float('INF')
    for v in itertools.permutations(lst):
        res = min(res, solve(v))

    print(res)