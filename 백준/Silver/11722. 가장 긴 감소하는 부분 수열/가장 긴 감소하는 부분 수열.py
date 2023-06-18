
if __name__ == '__main__':
    N = int(input())
    lst = list(map(int,input().split()))
    dp = [1] * N

    for i in range(N):
        for j in range(0,i):
            if lst[i] < lst[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    # print(dp)
    print(max(dp))