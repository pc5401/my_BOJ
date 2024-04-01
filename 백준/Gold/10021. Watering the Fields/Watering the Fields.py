import sys
import heapq 
input = sys.stdin.readline


def find_distances(i: tuple[int, int], j: tuple[int, int]) -> float | int:
    return (i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2


def solve(n: int, c: int, fields: list[tuple[int, int]]) -> float | int:
    # MST 구하기 단, 최소거리는 c 보다 커야한다.
    # Lazy Prim 알고리즘으로 풀이
    visited = [False] * n
    edges = [(0, 0)]
    res = 0

    while edges:
        cost, node = heapq.heappop(edges)
        if visited[node]:
            continue
        visited[node] = True
        res += cost
        for next in range(n):
            if not visited[next]:
                dist = find_distances(fields[node], fields[next])
                if dist >= c:
                    heapq.heappush(edges, (dist, next))
    
    if all(visited):
        return res
    else:
        return -1


def main():
    # 입력값
    N, C = map(int, input().split())
    fields = [tuple(map(int, input().split())) for _ in range(N)]
    # 풀이 후, 출력
    print(solve(N, C, fields))


if __name__ == "__main__":
    main()
