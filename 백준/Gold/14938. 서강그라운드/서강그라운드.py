import sys
import heapq
import collections

input = sys.stdin.readline
INF = float('INF')

def dijkstra(start: int, n: int, graph: dict) -> list:
    distance = [INF] * (n + 1)
    distance[start] = 0
    Q = [(0, start)]
    
    while Q:
        dist, now = heapq.heappop(Q)
        if distance[now] < dist:
            continue
        for nxt, w in graph[now]:
            cost = dist + w
            if cost < distance[nxt]:
                distance[nxt] = cost
                heapq.heappush(Q, (cost, nxt))
    return distance

def solve(n: int, m: int, r: int, t: list[int], grahp: collections.defaultdict) -> int:
    items = [0] + t
    max_items = 0
    # 모든 지역을 시작점으로 데이크스트라 실행
    for i in range(1, n+1):
        distances = dijkstra(i, n, grahp)
        total = 0
        # 수색 범위 내에 있는 지역들의 아이템 합산
        for j in range(1, n+1):
            if distances[j] <= m:
                total += items[j]
        max_items = max(max_items, total)
    
    return max_items


def main():
    # 입력
    n, m, r = map(int, input().split())
    t = list(map(int, input().split()))
    graph = collections.defaultdict(list)
    for _ in range(r):
        a, b, i = map(int, input().split())
        graph[a].append((b, i))
        graph[b].append((a, i))


    # 풀이
    result = solve(n, m, r, t, graph)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()
