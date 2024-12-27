import sys
input = sys.stdin.readline


def solve(N: int, A: list[int]) -> int:
    MOD = 1_000_000_007
    sumV, rtn = 0, 0

    for i in reversed(range(N)):
        rtn = (rtn + A[i] * sumV) % MOD
        sumV = (sumV + A[i]) % MOD

    return rtn


if __name__ == '__main__':
    # 입력값
    N = int(input())
    A = list(map(int, input().split()))

    # 풀이
    result = solve(N, A)

    # 출력
    print(result)