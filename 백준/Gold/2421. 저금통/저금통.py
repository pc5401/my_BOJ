import sys
input = sys.stdin.readline

def solve(N: int) -> int:
    M = 10**6
    is_prime = [True] * (M+1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(M**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, M+1, i):
                is_prime[j] = False

    tenpow = [1] * (N+1)
    for b in range(1, N+1):
        if b < 10:
            tenpow[b] = 10
        elif b < 100:
            tenpow[b] = 100
        else:
            tenpow[b] = 1000

    dp = [[0] * (N+2) for _ in range(N+2)]
    for a in range(N, 0, -1):
        for b in range(N, 0, -1):
            if a == N and b == N:
                dp[a][b] = 0
            else:
                best = 0
                if a < N:
                    best = dp[a+1][b]
                if b < N:
                    best = max(best, dp[a][b+1])
                val = a * tenpow[b] + b
                dp[a][b] = best + (1 if is_prime[val] else 0)

    return dp[1][1] - (1 if is_prime[11] else 0)

def main():
    # 입력
    N = int(input().strip())
    # 풀이
    result = solve(N)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
