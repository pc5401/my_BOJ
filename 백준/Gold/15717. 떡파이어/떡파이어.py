import sys
input = sys.stdin.readline

MOD = 1_000_000_007

def solve(N):
    if N == 0:
        return 1
    return pow(2, N - 1, MOD)

def main():
    # 입력
    N = int(input().strip())

    # 풀이
    ans = solve(N)

    # 출력
    print(ans)

if __name__ == "__main__":
    main()
