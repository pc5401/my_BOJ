import sys
input = sys.stdin.readline

def solve(N):
    return (N + 1) * N * (N - 1) // 2

def main():
    # 입력
    N = int(input().strip())

    # 풀이
    result = solve(N)

    # 출력
    print(result)

if __name__ == "__main__":
    main()
