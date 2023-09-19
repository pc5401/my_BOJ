import sys
input = sys.stdin.readline
        

def is_road(grassland, x1, y1, x2, y2):
    return f"{x1}_{y1}_{x2}_{y2}" in grassland or f"{x2}_{y2}_{x1}_{y1}" in grassland


def pasture(cow, N, grassland):
    visited = [[0]*N for _ in range(N)]
    cow[0] -= 1
    cow[1] -= 1
    visited[cow[0]][cow[1]] = 1
    stack = [cow]

    while stack:
        v = stack.pop()

        for d in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni = v[0] + d[0]
            nj = v[1] + d[1]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                if is_road(grassland, v[0], v[1], ni, nj):
                    continue
                visited[ni][nj] = 1
                stack.append([ni, nj])
    
    return visited


def count_result(idx, cows, visited, K):
    rtn = 0
    
    for i in range(idx+1, K):
        r, c = cows[i]
        if visited[r-1][c-1] == 0:
            rtn += 1

    return rtn


if __name__ == "__main__":
    # 입력 & 전처리
    N, K, R = map(int,input().split())
    grassland = set()
    for _ in range(R):
        r1, c1, r2, c2 = map(int, input().split())
        grassland.add(f"{r1-1}_{c1-1}_{r2-1}_{c2-1}")
    cows = [list(map(int, input().split())) for _ in range(K)]
    result = 0

    for cow_idx in range(K-1):
        visited_land = pasture(cows[cow_idx], N, grassland)
        result += count_result(cow_idx, cows, visited_land, K)

    print(result)