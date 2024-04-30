import sys
input = sys.stdin.readline


def solve(s: int, k: int) -> int:
    d, m = divmod(s, k)
    return d ** (k-m) * (d+1) **m


def main():
    # 입력값
    S, K = map(int, input().split())
    S: int
    K: int
    # 풀이
    result = solve(S, K)
    # 출력
    print(result)


if __name__ == "__main__":
    main()