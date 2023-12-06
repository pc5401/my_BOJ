import sys
import heapq
input = sys.stdin.readline

def solve(n: int, cave: list):
    distance = [[1e9] * (n) for _ in range(n)]
    Q = []
    heapq.heappush(Q, (cave[0][0], 0, 0))
    distance[0][0] = cave[0][0]

    while Q:
        dist, nowX, nowY = heapq.heappop(Q)

        if distance[nowX][nowY] < dist:
            continue

        for d in [(0,1),(1,0),(0,-1),(-1,0)]:
            ni = nowX + d[0]
            nj = nowY + d[1]
            if 0 <= ni < n and 0 <= nj < n:
                cost = dist + cave[ni][nj]
                if cost < distance[ni][nj]:
                    distance[ni][nj] = cost
                    heapq.heappush(Q, (cost, ni, nj))
    
    return distance[n-1][n-1]


if __name__ == "__main__":
    result = []
    while 1:
        N = int(input())
        if N == 0:
            break
        cave = [list(map(int, input().split())) for _ in range(N)]
        result.append(solve(N, cave))

    for idx, res in enumerate(result):
        print(f'Problem {idx+1}: {res}')