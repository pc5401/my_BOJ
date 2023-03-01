import sys
input = sys.stdin.readline
N = int(input())
lst = [0] * 710
res = 100

for i in range(710):
    lst[i] = i * ( 2 * i -1 )
    
dp = [ _ for _ in range(1000001)]

if N < 6:
    pass
else:
    for i in range(6,N+1):
        minV = 10
        for j in lst:
            if j > i:
                break
            minV = min(minV, dp[i-j] + 1)
        dp[i] = minV

print(dp[N])