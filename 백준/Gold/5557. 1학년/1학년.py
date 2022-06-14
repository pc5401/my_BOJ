# 구글링을 했다.

N = int(input())
lst = list(map(int, input().split()))

dp = [[0] * 21 for n in range(N)]  # 리스트가 인덱스 20까지인 길이가 N인 dp 리스트

dp[0][lst[0]] += 1  # 1 입력력
for i in range(1, N-1):
    for j in range(21): # 범위가 정해져서 가능함.
        if dp[i - 1][j]:  # 이전 값이 있으면,
            if j + lst[i] <= 20: dp[i][j + lst[i]] += dp[i - 1][j]
            if j - lst[i] >= 0: dp[i][j - lst[i]] += dp[i - 1][j]

print(dp[N - 2][lst[N - 1]])