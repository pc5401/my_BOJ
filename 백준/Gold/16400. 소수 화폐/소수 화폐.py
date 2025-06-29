import sys
input = sys.stdin.readline
MOD = 123456789

def solve(N: int) -> int:
    # 에라토스테네스 체
    sieve = [True] * (N+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(N**0.5)+1):
        if sieve[i]:
            step = i
            for j in range(i*i, N+1, step):
                sieve[j] = False
    primes = [i for i, is_p in enumerate(sieve) if is_p]
    
    dp = [0] * (N+1)
    dp[0] = 1
    for p in primes:
        for x in range(p, N+1):
            dp[x] = (dp[x] + dp[x - p]) % MOD
    return dp[N]

def main():
    # 입력
    N = int(input().strip())
    # 풀이
    result = solve(N)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
