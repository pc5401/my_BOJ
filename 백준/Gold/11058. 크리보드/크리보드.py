import sys
input = sys.stdin.readline

def solve(N: int) -> int:
    if N <= 6:
        return N
    
    dp = [i for i in range(N+1)]

    for i in range(7, N+1):
        dp[i] = dp[i-1] + 1

        for j in range(i-3, 0, -1):
            now = dp[j] * (i - j - 1)
            dp[i] = max(dp[i], now)

    return dp[N]



if __name__ == "__main__":
    # 입력값
    N = int(input())
    
    # 풀이 
    result = solve(N)
    
    # 출력
    print(result)
