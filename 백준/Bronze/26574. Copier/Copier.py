import sys
input = sys.stdin.readline


def solve(N: int, A: list[int]) -> int:
    return '\n'.join([f'{a} {a}' for a in A])


if __name__ == '__main__':
    # 입력값
    N = int(input())
    A = [int(input()) for _ in range(N)]

    # 풀이
    result = solve(N, A)

    # 출력
    print(result)