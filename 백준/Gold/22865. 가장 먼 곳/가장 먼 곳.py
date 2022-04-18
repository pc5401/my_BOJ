from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    distance = [1e9] * (N + 1)
    q = []
    #  시작 노드에 대해서 초기화
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance


N = int(input()) # 자취할 후보 개수
A, B, C = map(int, input().split())  # 사는 곳
M = int(input())
graph = defaultdict(list)

for _ in range(M):
    D, E, L = map(int, input().split())
    graph[D].append([E, L])
    graph[E].append([D, L])

distA = dijkstra(A)
distB = dijkstra(B)
distC = dijkstra(C)

maxV = res = 0
for i in range(1, N+1):
    minV = min(distA[i], distB[i], distC[i])  # 가까운 거리
    if minV > maxV:
        maxV = minV
        res = i

print(res)