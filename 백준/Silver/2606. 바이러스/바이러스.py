from collections import defaultdict


c = int(input()) # 컴퓨터 수
n = int(input())
data = defaultdict(list)
for _ in range(n):
    x, y = map(int, input().split())
    data[x].append(y)
    data[y].append(x)

lst = [0]*(c+1)


def dfs(x):
    lst[x] = 1

    for i in data[x]:
        if not lst[i]:
            dfs(i)


dfs(1)
lst[0] = 0
print(lst.count(1)-1)

