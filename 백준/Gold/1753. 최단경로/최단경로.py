import sys
import heapq

input = sys.stdin.readline
INF = 1e10
V, E = map(int, input().split())  # v 정점 수(1~20,000), e 간선 수(1~300,000)
k = int(input())  # 출발점
road_map = [[] for _ in range(V + 1)]
for _ in range(E):  # 간선 받기
    u, v, w = map(int, input().split())
    road_map[u].append((v, w))  # u가 노드 위치, v는 연결된 정점, w 가 가중치(거리)

dist = [INF]*(V+1)  # 빈 리스트, 거리 입력용

Q = []
def dijkstra(st_node):  # 출발 노드 입력
    dist[st_node] = 0
    heapq.heappush(Q, (0, st_node))

    while Q:  # Q가 빌때까지 탐색

        d, now = heapq.heappop(Q)  # d 거리, now 현위치

        for node, road_len in road_map[now]:  # n 연결 정점, w 가중치(거리)
            cost = d + road_len  # 비용 계산
            if cost < dist[node]:  # 비교, 이 경로가 만약 더 가까우면
                dist[node] = cost  # 바꿔치기
                heapq.heappush(Q, (cost, node))  # 새로운 heappush

dijkstra(k)  # k : 출발점
for i in dist[1:]:
    if i != INF:
        print(i)
    else:
        print('INF')