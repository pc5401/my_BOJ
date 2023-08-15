import sys
input = sys.stdin.readline


def fibo(n: int) -> int:
    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[-1]

if __name__ == '__main__':
    print(fibo(int(input())))
