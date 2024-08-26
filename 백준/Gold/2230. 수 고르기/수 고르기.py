import sys
input = sys.stdin.readline


def solve(N: int, M: int, A: list[int]) -> int:
    A = sorted(A)
    rtn = float('INF')
    lo, hi = 0, 0

    while hi < N and lo <= hi:
        diff = A[hi] - A[lo]
        if diff == M:
            return M
        elif diff > M:
            rtn = min(rtn, diff)
            lo += 1
        else:
            hi += 1

    return rtn

def main():
    # 입력값
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    # 풀이
    result = solve(N, M, A)

    # 출력
    print(result)


if __name__ == "__main__":
    main()