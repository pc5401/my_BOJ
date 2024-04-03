import sys
import collections
input = sys.stdin.readline


def dfs(idx: int, graph: collections.defaultdict[list[int]], visited: list[list[int]]):
    Q = [idx]

    while Q:
        v = Q.pop()
        visited[idx][v] = True
        visited[v][idx] = True
        
        for next in graph[v]:
            if not visited[idx][next]:
                Q.append(next)


def solve(n: int, graph: collections.defaultdict[list[int]]) -> int:
    visited = [[False]*n for _ in range(n)]

    for i in range(n):
        dfs(i, graph, visited)
    
    for i in range(n):
        if all(visited[i]):
            return i+1

    return -1


def main():
    # 입력값
    N = int(input())
    graph = collections.defaultdict(list)
    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
    # 풀이 후, 출력

    print(solve(N, graph))


if __name__ == "__main__":
    main()
