n, k = map(int, input().split()) # 입력 세팅
data = []
for i in range(n):
    v = int(input())
    data.append(v)

INF = 1e9 # 큰값

# dp 리스트 세팅
dp = [INF] * (k+1)
dp[0] = 0

for i in data:
    for j in range(i,k+1):
        dp[j] = min(dp[j], dp[j-i]+1)

res = dp[k] if dp[k] != INF else -1
print(res)