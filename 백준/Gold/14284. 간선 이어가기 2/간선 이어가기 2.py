import heapq
import sys

input = sys.stdin.readline

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: 

        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


INF = 1e9

n, m = map(int, input().split())
graph = [[] for i in range(n + 1)] # 노드 정보 리스트
distance = [INF] * (n + 1) # 체크하는 목적의 리스트

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

start, end = map(int,input().split()) # 시작, 끝 받기

# 다익스트라 알고리즘 수행
dijkstra(start)

res = distance[end]

print(res)