import sys
input = sys.stdin.readline
MOD = 10**6

def solve(N: int) -> int:
    dp = [[0]*3 for _ in range(2)]
    dp[0][0] = 1
    for _ in range(N):
        next_dp = [[0]*3 for _ in range(2)]
        for l in range(2):
            for a in range(3):
                val = dp[l][a]
                if not val:
                    continue
                    
                next_dp[l][0] = (next_dp[l][0] + val) % MOD
                
                if l == 0:
                    next_dp[1][0] = (next_dp[1][0] + val) % MOD

                if a < 2:
                    next_dp[l][a+1] = (next_dp[l][a+1] + val) % MOD
        dp = next_dp

    result = sum(dp[l][a] for l in range(2) for a in range(3)) % MOD
    return result

def main():
    # 입력
    N = int(input().strip())
    # 풀이
    result = solve(N)
    # 출력
    print(result)

if __name__ == "__main__":
    main()
