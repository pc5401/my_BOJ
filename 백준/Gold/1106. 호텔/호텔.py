import sys
input = sys.stdin.readline

C,N = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(N)]
lst.sort() # 오름차순 정렬
dp = [0] + [1e7] * (C + 100)
res = 1e7
for c, p in lst: # c=cost(비용), p=people(고객, 사람)
    for i in range(p, len(dp)):
        dp[i] = min(dp[i-p] + c, dp[i])
        if i >= C:
            res = min(dp[i], res)
    # print(dp)
print(res)