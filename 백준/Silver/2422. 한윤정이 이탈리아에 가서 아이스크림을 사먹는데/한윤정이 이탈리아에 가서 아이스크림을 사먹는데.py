import sys

input = sys.stdin.readline


def solve(N: int, M: int, no_ice: set[tuple[int]]) -> int:
    rtn = 0

    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if (i, j) in no_ice or (j, i) in no_ice:
                continue
            for k in range(j+1, N+1):
                if (i, k) in no_ice or (j, k) in no_ice:
                    continue
                if (k, i) in no_ice or (k, j) in no_ice:
                    continue
                rtn += 1
    return rtn


def main():
    # 입력값
    N, M = map(int, input().split())
    no_icecream: set[tuple[int]] = {tuple(map(int, input().split())) for _ in range(M)}
    # 풀이
    result: str = solve(N, M, no_icecream)
    # 출력
    print(result)


if __name__ == "__main__":
    main()