def dfs(arr):
    global minV, res

    if len(arr) >= 3:
        sumV = sum(arr)
        ans = M - sumV
        if ans >= 0 and minV > ans:
            minV = ans
            res = sumV
        return

    for i in lst:
        if i not in arr:
            dfs(arr+[i])


N, M = map(int, input().split())
lst = list(map(int, input().split()))
minV = 1e9
res = 0
for l in lst:
    dfs([l])

print(res)