import sys
input = sys.stdin.readline


def solve(N: int, R: int):
    rtn = N - 1
    rtn += (R*2)
    return rtn


def main():
    N, R = map(int, input().split())
    print(solve(N, R))

main()


