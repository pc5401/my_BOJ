import sys
input = sys.stdin.readline


if __name__ == '__main__':
    mod = 1_000_000_000
    n = int(input())
    if n < 10:
        print(0)
        quit()

    # 1차원 n개, 2차원 0~9, 3차원 비트마스킹 2^10
    dp = [[[0]*1024 for _ in range(10)] for _ in range(n+1)]

    # 각 숫자를 마지막 숫자로 하는 길이 1의 계단 수로 초기화
    for i in range(1, 10):
        dp[1][i][1 << i] = 1
    
    # 길이가 2 이상인 계단 수를 계산
    for i in range(2, n+1):
        for j in range(10):
            for k in range(1024):
                if j > 0: # 0 빼고 -1
                    dp[i][j][k | 1 << j] += dp[i-1][j-1][k]
                if j < 9: # 9 빼고 +1
                    dp[i][j][k | 1 << j] += dp[i-1][j+1][k]
                dp[i][j][k | 1 << j] %= mod

    print(sum(dp[n][i][1023] for i in range(10)) % mod)