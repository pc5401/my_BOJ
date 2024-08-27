import sys
input = sys.stdin.readline


def solve(N: int, K: int) -> int:
    v = (K * (K+1)) // 2

    if K >= N or N < v:
        return -1

    return K if (N - v) % K else K-1


def main():
    # 입력값
    N, K = map(int, input().split())
    
    # 풀이
    result = solve(N, K)

    # 출력
    print(result)


if __name__ == "__main__":
    main()