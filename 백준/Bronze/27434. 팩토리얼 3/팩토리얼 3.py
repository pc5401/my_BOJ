import sys
input = sys.stdin.readline


def solve(N: int):
    if N < 2:
        return 1

    rtn = 1

    for i in range(2, N+1):
        rtn *= i

    return rtn


def main():
    N = int(input())
    print(solve(N))

main()


