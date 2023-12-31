import sys
import heapq
import collections
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    eyes = list(map(int,input().split()))
    loads = collections.defaultdict(list)
    for _ in range(M):
        a, b, t = map(int,input().split())
        loads[a].append((b,t))
        loads[b].append((a,t))
    
    distance = [float('INF')] * N
    queue = [(0,0)]
    distance[0] = 0

    while queue:
        time, now = heapq.heappop(queue)

        if distance[now] < time:
            continue

        for next, dist in loads[now]:
            cost = time + dist
            
            if eyes[now] and not now == (N-1):
                continue
            
            if distance[next] > cost:
                distance[next] = cost
                heapq.heappush(queue, (cost, next))
    
    if distance[-1] >= 1e10:
        print(-1)
    else:
        print(distance[-1])
