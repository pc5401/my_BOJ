import sys
input = sys.stdin.readline

N = int(input())
dp = [1,1,1]
res = sum(dp)

for i in range(2,N+1):
    x = dp[0]+ dp[1]
    y = res
    z = dp[1] + dp[2]
    res = x + y + z
    dp = [x,y,z]

print(res % 9901 )