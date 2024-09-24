import sys
input = sys.stdin.readline


def solve(n: int, a: list[int]) -> int:
    rtn = 0
    hi = a[-1]
    
    for i in range(n-1, -1, -1):
        if a[i] > hi:
            hi = a[i]
            continue

        if hi - a[i] > rtn:
            rtn = hi - a[i]

    return rtn


def main():
    # 입력값
    N = int(input())
    A = list(map(int, input().split()))
    
    # 풀이
    result = solve(N, A)

    # 출력
    print(result)


if __name__ == "__main__":
    main()
