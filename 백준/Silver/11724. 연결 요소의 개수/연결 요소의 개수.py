from collections import defaultdict
# import sys
# limit_number = 1500000
# sys.setrecursionlimit(limit_number)

gragh = defaultdict(list)
N,M = map(int, input().split())
visit = [0] * (N+1)
for _ in range(M):
    u, v = map(int,input().split())
    gragh[u].append(v)
    gragh[v].append(u)

cnt = 0


stack = []
def dfs(node):
    global cnt

    stack.append(node)
    while stack:
        v = stack.pop()
        
        for i in gragh[v]:
            if visit[i] == 0:
                stack.append(i)
                visit[i] = cnt


for idx in range(1,N+1):
    if visit[idx] == 0:
        cnt += 1
        visit[idx] = cnt
        dfs(idx)

print(max(visit))