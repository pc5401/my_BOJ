import sys
import heapq
input = sys.stdin.readline


def dijkstra(start): # 다익스트라
    global N
    
    distance = [1e9] * (N+1)
    que = [(0,start)] # 거리, 위치

    while que:
        dist, now = heapq.heappop(que)

        if distance[now] < dist:
            continue

        for i in range(1, N+1):
            if not graph[now][i]:
                continue

            if graph[now][i] + dist < distance[i]:
                distance[i] = graph[now][i] + dist
                heapq.heappush(que, (distance[i], i))

    return distance




if __name__ == '__main__':
    # 입력값 처리
    N, E = map(int,input().split())
    graph = [[0]*(N+1) for i in range(N+1)]
    for e in range(E):
        a,b,c = map(int,input().split())
        graph[a][b] = c
        graph[b][a] = c
    v_1, v_2 = map(int,input().split())

    one_dist = dijkstra(1)
    v_1_dist = dijkstra(v_1)
    v_2_dist = dijkstra(v_2)

    a_case = one_dist[v_1] + v_1_dist[v_2] + v_2_dist[N]
    b_case = one_dist[v_2] + v_2_dist[v_1] + v_1_dist[N]
    short_case = min(a_case, b_case)

    if v_1 == 1 and v_2 == N:
        short_case = min(short_case, one_dist[N])

    print(short_case if short_case < 1e9 else -1 )


