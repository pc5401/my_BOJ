import sys
import heapq
input = sys.stdin.readline


def make_graph(die: list, danger: list) -> list:
    grahp = [[0]*501 for _ in range(501)]

    for x1, y1, x2, y2 in danger:
        for i in range(min(x1, x2), max(x1, x2)+1):
            for j in range(min(y1, y2), max(y1, y2)+1):
                grahp[i][j] = 1

    for x1, y1, x2, y2 in die:
        for i in range(min(x1, x2), max(x1, x2)+1):
            for j in range(min(y1, y2), max(y1, y2)+1):
                grahp[i][j] = -1

    return grahp


def dijkstra(graph):
    distance = [[float('INF')]*501 for _ in range(501)]
    visited = [[False]*501 for _ in range(501)] 
    delta = ((0,1), (1,0), (0,-1), (-1,0))
    distance[0][0] = 0
    Q = [(0,0,0)]
    
    while Q:
        cost, x, y = heapq.heappop(Q)
        
        if visited[x][y]:
            continue
        visited[x][y] = 1

        for d in delta:
            ni = x + d[0]
            nj = y + d[1]
            if 0 <= ni < 501 and 0 <= nj < 501 and graph[ni][nj] >= 0:
                new_cost = cost + graph[ni][nj]
                if new_cost < distance[ni][nj]:
                    distance[ni][nj] = new_cost
                    heapq.heappush(Q, (new_cost, ni, nj))

    
    return distance


if __name__ == '__main__':
    N = int(input())
    danger = [list(map(int, input().split())) for _ in range(N)]
    M = int(input())
    die = [list(map(int, input().split())) for _ in range(M)]
    
    graph = make_graph(die, danger)
    distance = dijkstra(graph)
    print(distance[500][500] if distance[500][500] != float('inf') else -1)