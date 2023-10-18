import sys
input = sys.stdin.readline

MOD = 1_000_000_007

def solve(a: int, x: int) -> int:
    if x == 1:
        return a % MOD
    temp = solve(a, x // 2)
    if x % 2 == 0:
        return (temp * temp) % MOD
    else:
        return (temp * temp * a) % MOD

if __name__ == "__main__":
    # 입력 & 전처리
    A = int(input())
    X = int(input())

    print(solve(A, X))
