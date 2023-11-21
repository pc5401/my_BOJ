import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]

    for k in range(N): # 플로이드 워셜
        for i in range(N):
            for j in range(N):
                if T[i][j] > T[i][k] + T[k][j]:
                    T[i][j] = T[i][k] + T[k][j]

    Q = [[K, 0, 1<<K]]
    end = (1 << N) - 1
    result = 1001 * N

    while Q:

        now, distance ,visited = Q.pop()

        if distance >= result:
            continue

        if visited == end:
            result = distance
            continue

        for i in range(N):
            if visited & (1<<i):
                continue
            Q.append([i, distance+T[now][i], visited + (1<<i)])
    
    print(result)