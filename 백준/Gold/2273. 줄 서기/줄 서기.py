import sys
input = sys.stdin.readline

def solve(N: int, graph: list[list[int]]) -> list[list[int]]:
    # 플로이드 워셜
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1
    return graph


def result(N: int, graph: list[list[int]]):
    # 사이클이 있는지 확인
    for i in range(1, N+1):
        if graph[i][i]:  # 자기 자신에게 가는 경로가 있으면 사이클 발생
            print(-1)
            return

    # 각 학생이 설 수 있는 위치의 범위를 계산
    results = []
    for i in range(1, N+1):
        before = sum(graph[j][i] for j in range(1, N+1) if j != i)
        after = sum(graph[i][j] for j in range(1, N+1) if j != i)
        
        min_pos = before + 1
        max_pos = N - after
        results.append((min_pos, max_pos))
    
    for res in results:
        print(*res)
    

def main():
    # 입력값
    N, M = map(int, input().split())
    input_A_B = [map(int, input().split()) for _ in range(M)]
    graph = [[0]*(N+1) for _ in range(N+1)]
    for A, B in input_A_B:
        graph[A][B] = 1
    
    del input_A_B

    # # 풀이
    solve(N, graph)

    # # 출력
    result(N, graph)


if __name__ == "__main__":
    main()


