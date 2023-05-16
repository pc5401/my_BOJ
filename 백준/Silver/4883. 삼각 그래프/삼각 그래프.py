import sys
input = sys.stdin.readline

def work(n):
    # 최소비용
    dp = [list(map(int,input().split())) for _ in range(n)]
    # DP 초기화를 해줘야. 한다 첫 줄 가운데에서 시작하므로.
    dp[0][0] = 10100
    dp[0][2] += dp[0][1] 
    
    for i in range(1,n):
        dp[i][0] += min(dp[i-1][0], dp[i-1][1])
        dp[i][1] += min(dp[i-1][0], dp[i-1][1], dp[i-1][2], dp[i][0])
        dp[i][2] += min(dp[i-1][1], dp[i-1][2], dp[i][1])

    return dp[n-1][1]


if __name__ == "__main__":
    tc = 0
    while True:
        tc += 1
        N = int(input())
        if N:
            print(f'{tc}. {work(N)}')
        else:
            break
