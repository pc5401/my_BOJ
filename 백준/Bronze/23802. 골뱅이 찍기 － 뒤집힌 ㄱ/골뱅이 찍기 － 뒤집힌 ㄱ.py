import sys
input = sys.stdin.readline


def solve(N: int, A: list[int]) -> int:
    return '\n'.join([f'{a} {a}' for a in A])


if __name__ == '__main__':
    # 입력값
    N = int(input())

    for n in range(1, N+1):
        print('@@@@@' * N)
    
    for n in range(4*N):
        print('@'*N)