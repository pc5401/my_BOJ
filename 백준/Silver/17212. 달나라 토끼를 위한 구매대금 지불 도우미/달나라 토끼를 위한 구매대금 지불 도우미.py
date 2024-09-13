import sys
input = sys.stdin.readline

def get_dp(n: int) -> list[int]:
    dp = [i for i in range(n+1)]
    if n >= 2:
        dp[2] = 1
    
    if n >= 5:
        dp[5] = 1
    
    if n >= 7:
        dp[7] = 1
    
    return dp


def solve(n: int) -> int:
    dp = get_dp(n)

    for i in range(1, n):
        if i + 1 <= n:
            dp[i+1] = min(dp[i+1], dp[i]+1)
        if i + 2 <= n:
            dp[i+2] = min(dp[i+2], dp[i]+1)   
        if i + 5 <= n:
            dp[i+5] = min(dp[i+5], dp[i]+1)   
        if i + 7 <= n:
            dp[i+7] = min(dp[i+7], dp[i]+1)   
    
    return dp[n]

def main():
    # 입력값
    N = int(input())

    # 풀이
    result = solve(N)

    # 출력
    print(result)


if __name__ == "__main__":
    main()


