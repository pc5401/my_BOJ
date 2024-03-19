import sys
input = sys.stdin.readline

def make_travelable_map(n: int, graph: list[list[int]]) -> list[int]:
    visited = [[0] * n for _ in range(n)]
    
    for city in range(n):
        Q = [city]
        visited[city][city] = 1
        while Q:
            i = Q.pop()
            for j in range(n):
                if graph[i][j] and not visited[city][j]:
                    visited[city][j] = 1
                    Q.append(j)

    return visited


def result(m: int, plan: list[int], travelable_map: list[list[int]]) -> str:

    for i in range(m-1):
        curr, next = plan[i]-1, plan[i+1]-1
        if not travelable_map[curr][next]:
            return 'NO'

    return 'YES'


def main():
    N = int(input())
    M = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    plan = list(map(int, input().split()))
    travelable_map = make_travelable_map(N, graph)
    print(result(M, plan, travelable_map))

if __name__ == "__main__":
    main()


