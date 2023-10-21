import sys
input = sys.stdin.readline


def solve(n: int) -> tuple:
    MOD = 1_000_000
    table = [0,1,1]
    a, b = 1, 1
    if n < 3:
        return table, 3
    
    while True:
        a, b = b, (a+b) % MOD
        if a == 0 and b == 1:
            return table, len(table) - 1
        table.append(b)


if __name__ == "__main__":
    # 입력 & 전처리
    N = int(input())
    dp, M = solve(N)
    print(dp[N%M])
