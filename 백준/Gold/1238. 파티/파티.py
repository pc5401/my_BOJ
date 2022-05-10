import sys
input = sys.stdin.readline
import heapq

def dijkstra(start, end):
    # 시작 세팅
    distance = [1e9] * (N + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    # Q가 빌 때까지 or end 에 도착할 때까지.
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:  # 이미 최단거리라면
            continue

        for i in graph[now]:
            cost = dist + i[1]


            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    # print(distance)
    # print(distance[end])
    return distance[end]




N, M, X = map(int, input().split())
graph = [[] for n in range(N+1)]

for _ in range(M):
    s, e, t = map(int, input().split()) # s:시작점, e: 끝점, t: 거리
    graph[s].append((e, t)) # 단방향

maxV = 0
for n in range(1, N+1):
    # print(f'확인 n{n} X{X}')
    a = int(dijkstra(n, X))
    b = int(dijkstra(X, n))

    if a + b > maxV:
        maxV = (a + b)

print(maxV)