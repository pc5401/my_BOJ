n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
dy = [-10000] * n
dp[0]= arr[0]

minV = 0
for i in range(1, n):
    if dp[i-1] + arr[i] > 0 :
        dp[i] = max(dp[i-1]+arr[i], arr[i])
    else:
        dp[i] = arr[i]
    
    dy[i] = max(dp[i-1] , dy[i-1] + arr[i])


res1 = max(dp)
res2 = max(dy)
print(max(res1, res2))

