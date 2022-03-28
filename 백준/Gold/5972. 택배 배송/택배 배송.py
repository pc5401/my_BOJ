import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
INF = 1e10
arr = [[] for i in range(N+1)]  # 지도 정보

for i in range(M):
    A_i, B_i, C_i = map(int, input().split())
    arr[A_i].append((B_i, C_i))
    arr[B_i].append((A_i, C_i))

Q = []
distance = [INF] * (N+1)
def dijkstra(start):
    distance[start] = 0
    heapq.heappush(Q, (0, start))

    while Q:

        dist, tmp = heapq.heappop(Q)

        if distance[tmp] < dist:
            continue

        for cnx, wt in arr[tmp]:  # cnx(connect) : 연결점, wt(weight) : 가중치
            cost = dist + wt

            if cost < distance[cnx]:
                distance[cnx] = cost
                heapq.heappush(Q, (cost, cnx))

dijkstra(1)  # 시작점
res = distance[N]

print(res)