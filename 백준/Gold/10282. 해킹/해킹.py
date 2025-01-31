import sys
import heapq
import collections

input = sys.stdin.readline
INF = float('INF')

def dijkstra(start, distance, graph):
    Q = []

    heapq.heappush(Q, (0, start))
    distance[start] = 0

    while Q:
        dist, now = heapq.heappop(Q)

        if distance[now] < dist:
            continue

        for next, s in graph[now]:
            cost = dist + s
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(Q, (cost, next))

def solve(ndc: list[int], grahp: collections.defaultdict) -> int:
    n, d, c = ndc
    distance = [INF] * (n + 1)
    dijkstra(c, distance, grahp)

    cnt, time = 0, 0
    for i in range(1, n+1):
        if distance[i] == INF:
            continue
        cnt += 1
        time = max(distance[i], time)

    return (cnt, time)


def main():
    # 입력
    T = int(input())
    ndc_cast = []
    grahp_cast = []
    for _ in range(T):
        ndc = list(map(int, input().split()))
        ndc_cast.append(ndc)
        grahp = collections.defaultdict(list)
        for _ in range(ndc[1]):
            a, b, s = map(int, input().split())
            grahp[b].append((a, s))
        grahp_cast.append(grahp)

    # 풀이
    result = [solve(ndc_cast[t], grahp_cast[t]) for t in range(T)]
    
    # 출력
    for res in result:
        print(*res)

if __name__ == "__main__":
    main()
