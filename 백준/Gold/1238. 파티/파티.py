import sys
import collections
import heapq
input = sys.stdin.readline

def dijkstra(start: int, N: int, end:int) -> list:
    distance = [1e9] * N
    distance[start] = 0
    Q = []
    heapq.heappush(Q, (0, start))

    while Q:
        now_cost, now = heapq.heappop(Q)
        
        if distance[now] < now_cost:
            continue
        
        for next, next_cost in dp[now]:
            cost = now_cost + next_cost
            if distance[next] > cost:
                distance[next] = cost
                heapq.heappush(Q, (cost, next))

    return distance[end]

if __name__ == "__main__":
    N, M, X = map(int, input().split())
    dp = collections.defaultdict(list)
    for _ in range(M):
        A, B, T = map(int, input().split())
        dp[A-1].append((B-1,T))

    res = 0

    for i in range(N):
        a = dijkstra(X-1, N,  i)
        b = dijkstra(i, N, X-1)
        res = max(res, a+b)
    
    print(res)