import sys
input = sys.stdin.readline      


def solve(N: int) -> int:
    return N * (N-1)


if __name__ == "__main__":
    # 입력값
    N = int(input())
    
    # 풀이
    result = solve(N)

    # 출력
    print(result)