n = int(input())
dp = [0] * 31 

if n %2:
    print(0)
    quit()

dp[0] = 1
dp[2] = 3

for i in range(4, 31, 2):
    dp[i] = 3*dp[i-2]
    for j in range(i-4,-1,-2):
        dp[i] += dp[j]*2

print(dp[n])