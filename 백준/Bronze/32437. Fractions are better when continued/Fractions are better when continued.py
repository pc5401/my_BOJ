import sys
input = sys.stdin.readline

def solve(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b

    return b

if __name__ == "__main__":
    # 입력값
    N = int(input())

    # 풀이
    result = solve(N)

    # 출력
    print(result)