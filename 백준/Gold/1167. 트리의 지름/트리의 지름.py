from collections import defaultdict
import sys
input = sys.stdin.readline

def dfs(n):
    global V

    visit = [0] * (V+1)
    visit[n] = 1
    Q = [n]
    r = [0,0]
    while Q:
        v = Q.pop()

        for nod, dir in graph[v]:
            if visit[nod]:
                continue
            visit[nod] = visit[v] + dir
            Q.append(nod)
            if visit[nod] > r[0]:
                r[0],r[1] = visit[nod],nod

    return r


graph = defaultdict(list)
V = int(input())
for _ in range(V): # 입력 처리
    lst = list(map(int,input().split()))
    node = lst[0]
    lLen = len(lst)
    for i in range(1,lLen ,2):
        if lst[i] == -1 or i+1 >= lLen:
            break
        graph[node].append([lst[i], lst[i+1]]) # 연결 node, node 거리

res, spot = dfs(1)
res, spot = dfs(spot)

print(res-1)