import sys
input = sys.stdin.readline

def solve(A: int, B: int, N: int, routes: list[tuple[int, list[int]]]) -> int:
    result = None
    # 각 항공 경로를 확인
    for cost, cities in routes:
        try:
            idxA = cities.index(A)
        except ValueError:
            continue
        try:
            idxB = cities.index(B)
        except ValueError:
            continue
        # A가 B보다 앞에 있어야 함
        if idxA < idxB:
            if result is None or cost < result:
                result = cost
    return result if result is not None else -1

def main():
    # 입력
    A, B, N = map(int, input().split())
    routes = []
    for _ in range(N):
        cost, num = map(int, input().split())
        cities = list(map(int, input().split()))
        routes.append((cost, cities))
    
    # 풀이
    result = solve(A, B, N, routes)
    
    # 출력
    print(result)

if __name__ == "__main__":
    main()
