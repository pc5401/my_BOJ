import sys
input = sys.stdin.readline


#  1660 번
if __name__ == "__main__":
    N = int(input())
    dp = [i for i in range(N+1)]
    lst = [(i * (i+1)) // 2  for i in range(1, 122)]
    for i in range(1,121):
        lst[i] += lst[i-1]
    
    for i in range(1, N+1):
        for j in range(i):
            if lst[j] > i:
                break
            dp[i] = min(dp[i], dp[i - lst[j]] + 1)

    print(dp[N])