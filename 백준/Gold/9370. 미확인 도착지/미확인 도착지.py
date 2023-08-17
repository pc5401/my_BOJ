import sys
import heapq
input = sys.stdin.readline

def dijkstra(start, n):
    
    distance = [INF] * (n + 1)
    que = []
    #  시작 노드에 대해서 초기화
    heapq.heappush(que, (0, start))
    distance[start] = 0
    while que: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(que)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in range(1, n+1):
            if graph[now][i] == 0:
                continue
            cost = dist + graph[now][i]

            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(que, (cost, i))

    return distance

if __name__ == '__main__':
    INF = int(1e9)
    TC = int(input())
    for _ in range(TC):
        N, M, T = map(int, input().split()) 
        graph = [[0]*(N+1) for n in range(N+1)]
        S, G, H = map(int, input().split()) 
        for m in range(M): 
            A, B, D = map(int, input().split()) 
            graph[A][B] = D
            graph[B][A] = D

        X_lst = [int(input()) for t in range(T)] # 확인 값
        S_distance = dijkstra(S, N) 
        G_distance = dijkstra(G, N)
        H_distance = dijkstra(H, N)
        
        res = []
        for x in X_lst:
            GH = S_distance[G] + graph[G][H] + H_distance[x]
            HG = S_distance[H] + graph[H][G] + G_distance[x]
            
            if S_distance[x] == min(GH, HG):
                res.append(x)
        
        print(*sorted(res))
