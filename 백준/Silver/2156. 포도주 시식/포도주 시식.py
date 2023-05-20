import sys
input = sys.stdin.readline

def dp_solve(n:int) -> int:
    dp = [0] * n
    dp[0],dp[1] = arr[0], arr[0] + arr[1] 
    for i in range(2,n):
        dp[i] = (max(dp[i-1], # 이전꺼만 마시고
                    dp[i-2] + arr[i], # 현재 잔 마시고, 그 이전꺼까지 max
                    dp[i-3] + arr[i-1] + arr[i])) # 현재 잔 마시고, 그 이전꺼만 마시고
                    # 먄약 i = 2이면 dp[i-3] = dp[-1] = 0
    return dp[-1]


if __name__ == "__main__":
    N = int(input())
    arr = [int(input()) for i in range(N)]
    if N < 2:
        print(sum(arr))
    else:
        print(dp_solve(N))