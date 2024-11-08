import sys
input = sys.stdin.readline


def solve(n: int, dp: list[int]) -> int:
    if dp[0] >= n:
        return dp[n]

    for i in range(dp[0]+1, n+1):
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1_000_000_009
    
    dp[0] = n
    return dp[n]
    

def main():
    # 입력값
    T = int(input())
    N = [int(input()) for _ in range(T)]
    
    # 풀이
    dp = [0] * (1_000_001)
    dp[0] = 3
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    result = [solve(n, dp) for n in N]
    
    # 출력 
    for res in result:
        print(res)

if __name__ == '__main__':
    main()
