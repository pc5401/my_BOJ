import sys
import heapq
input = sys.stdin.readline


if __name__ == '__main__':
    # 입력값 처리
    M, N = map(int,input().split())
    graph = [list(map(int, input().rstrip('\n'))) for _ in range(N)]
    distance = [[1e9] * (M) for _ in range(N)]
    distance[0][0] = 0
    
    que = [[0, [0, 0]]]
    
    while que:

        dist, now = heapq.heappop(que) # x가 세로, y가 가로
        x, y = now
        if distance[x][y] < dist:
            continue

        for d in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni = x + d[0]
            nj = y + d[1]
            if 0 <= ni < N and 0 <= nj < M:

                now_dist = distance[x][y] + graph[ni][nj]
                if distance[ni][nj] > now_dist:
                    distance[ni][nj] = now_dist
                    heapq.heappush(que, [now_dist, [ni, nj]])

    print(distance[-1][-1])