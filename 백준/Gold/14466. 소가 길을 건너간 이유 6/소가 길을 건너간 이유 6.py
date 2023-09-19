from collections import deque

def is_road(grassland, x1, y1, x2, y2):
    return f"{x1}_{y1}_{x2}_{y2}" in grassland or f"{x2}_{y2}_{x1}_{y1}" in grassland

def pasture(start_x, start_y, N, grassland):
    visited = [[False]*N for _ in range(N)]
    visited[start_x][start_y] = True
    queue = deque([(start_x, start_y)])

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if is_road(grassland, x, y, nx, ny):
                    continue
                visited[nx][ny] = True
                queue.append((nx, ny))

    return visited

if __name__ == "__main__":
    N, K, R = map(int, input().split())
    grassland = set()
    for _ in range(R):
        r1, c1, r2, c2 = map(int, input().split())
        grassland.add(f"{r1-1}_{c1-1}_{r2-1}_{c2-1}")

    cows = [tuple(map(int, input().split())) for _ in range(K)]
    cnt = 0

    for i in range(K):
        x1, y1 = cows[i]
        visited = pasture(x1 - 1, y1 - 1, N, grassland)
        for j in range(i + 1, K):
            x2, y2 = cows[j]
            if not visited[x2 - 1][y2 - 1]:
                cnt += 1

    print(cnt)