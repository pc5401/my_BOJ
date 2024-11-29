import sys
from functools import reduce
input = sys.stdin.readline

def solve(N: int, A: list[int]) -> int:
    rtn = 0

    for a in range(1, N-2):
        for b in range(a+1, N-1):
            for c in range(b+1, N):
                q = reduce(lambda acc, cur : acc * cur ,A[0:a], 1) 
                w = reduce(lambda acc, cur : acc * cur ,A[a:b], 1) 
                e = reduce(lambda acc, cur : acc * cur ,A[b:c], 1) 
                r = reduce(lambda acc, cur : acc * cur ,A[c:N], 1)
                rtn = max(rtn, q+w+e+r)

    return rtn


    
def main():
    # 입력값
    N = int(input())
    A = list(map(int, input().split()))

    # 풀이
    result = solve(N, A)

    # 결과 출력
    print(result)
        
if __name__ == '__main__':
    main()