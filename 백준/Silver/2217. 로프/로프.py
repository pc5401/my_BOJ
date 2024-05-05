import sys
input = sys.stdin.readline


def solve(N: int, lopes: list[int]) -> int:
    rtn = 0

    for i in range(N):
        rtn = max(rtn, lopes[i] * (N-i))

    return rtn


def main():
    # 입력값
    N = int(input())
    lopes = [int(input()) for _ in range(N)]
    lopes.sort()

    # 풀이
    result = solve(N, lopes)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()
