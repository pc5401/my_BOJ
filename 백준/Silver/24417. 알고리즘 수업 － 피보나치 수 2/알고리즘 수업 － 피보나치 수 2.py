import sys
input = sys.stdin.readline


def solve(n: int) -> int:
    a, b = 2, 3
    for i in range(4, n):
        a, b = b, (a+b) % 1000000007
    
    return b


if __name__ == "__main__":
    # 입력값
    N = int(input())

    # 풀이
    result = solve(N)
    
    # 출력    
    print(result, N-2)