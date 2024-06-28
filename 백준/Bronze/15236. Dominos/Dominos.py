import sys
input = sys.stdin.readline


def solve(n: int) -> int:
    rtn = 0
    for i in range(n+1):
        for j in range(i, n+1):
            rtn += (i+j)

    return rtn


def main():
    # 입력값
    N = int(input())
    # 풀이
    result: int = solve(N)
    # 출력
    print(result)


if __name__ == "__main__":
    main()