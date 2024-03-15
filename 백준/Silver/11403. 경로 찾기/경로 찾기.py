import sys
input = sys.stdin.readline


def dfs(node, next,n,graph,visited):
    visited[node][next] = 1
    
    Q = [next]

    while Q:
        i = Q.pop()

        for j in range(n):
            if graph[i][j] and not visited[node][j]:
                visited[node][j] = 1
                Q.append(j)


def main():
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited =[[0]*N for _ in range(N)]
    for node in range(N):
        for next in range(N):
            if graph[node][next] and not visited[node][next]:
                dfs(node, next, N, graph, visited)

    for visit in visited:
        print(*visit)

if __name__ == "__main__":
    main()
