import sys
import collections
import heapq
input = sys.stdin.readline

def solve(N: int, in_degree: list[int], graph:collections.defaultdict) -> list[int]:
    rtn = []
    Q = []

    for i in range(1, N+1):
        if in_degree[i] == 0:
            Q.append(i)
    
    heapq.heapify(Q)

    while Q:
        v = heapq.heappop(Q)
        rtn.append(v)

        for j in graph[v]:
            in_degree[j] -= 1
            if in_degree[j] == 0:
                heapq.heappush(Q, j)

    return rtn


def main():
    # 입력값
    N, M = map(int, input().split())
    in_degree = [0] * (N+1)
    graph = collections.defaultdict(list)
    for _ in range(M):
        A, B = map(int, input().split())
        in_degree[B] += 1
        graph[A].append(B)

    # 풀이
    result = solve(N, in_degree, graph)
    # 출력
    print(*result)


if __name__ == "__main__":
    main()

