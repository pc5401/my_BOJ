import sys
import heapq
import collections
input = sys.stdin.readline


def dijkstra(n, start, graph) -> list:
    distance = [1e9] * (n+1)
    Q = []
    distance[start] = 0
    heapq.heappush(Q, (0, start))

    while Q:

        dist, now = heapq.heappop(Q)

        if distance[now] < dist:
            continue

        for next in graph[now]:
            cost = dist + 1
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(Q, (cost, next))

    return distance

if __name__ == "__main__":
    N, M, K, X = map(int, input().split())
    graph = collections.defaultdict(list)
    for _ in range(M):
        A, B = map(int, input().split())
        graph[A].append(B)
    
    result = []
    lst = dijkstra(N, X, graph)
    for n, v in enumerate(lst):
        if v == K:
            result.append(n)
    
    if result:
        for res in result:
            print(res)
    else:
        print(-1)