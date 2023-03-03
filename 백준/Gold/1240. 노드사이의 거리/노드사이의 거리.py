from collections import defaultdict
import sys
input = sys.stdin.readline

def dfs(x,y):
    global N

    q = [x]
    visit = [0] * (N+1)

    while q:
        v = q.pop()
        if v == y:
            return visit[y]

        for i, l in enumerate(nodes[v][1:],start=1):
            if not l or visit[i]:
                continue
            visit[i] = visit[v] + l
            q.append(i)


N, M = map(int,input().split())
nodes = [[0]*(N+1) for _ in range(N+1)]
for _ in range(N-1):
    a,b,l = map(int,input().split())
    nodes[a][b] = l
    nodes[b][a] = l

for _ in range(M):
    a,b = map(int,input().split())
    res = dfs(a,b)
    print(res)