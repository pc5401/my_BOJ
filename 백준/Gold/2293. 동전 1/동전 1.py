n, k = map(int, input().split())
data = []
for i in range(n):
    v = int(input())
    data.append(v)

dp = [0] * (k+1)
dp[0] = 1

for i in data:
    for j in range(i, k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]

    # print(dp)
print(dp[k])