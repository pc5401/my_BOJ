def dfs(num, lst):
    global m, n

    lst.append(num)

    if len(lst) >= m:
        return print(*lst)

    for i in range(num+1,n+1):
        dfs(i, lst[:])



n, m =map(int,input().split())

for i in range(1, n+1):
    dfs(i, [])